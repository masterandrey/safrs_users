"""
Common code to keep api handler DRY
"""
import db.conn
from journaling import log
from controllers.models import APIError
import re
import inspect
import functools
import traceback
from controllers.models import AuthUser
import schematics.exceptions
from controllers.models import API_ERROR_CODE, UNHANDLED_EXC_CODE, SUCCESS_CODE, NO_TOKEN_CODE


def transaction(handler):
    """
    Decorator to wrap api handler into try-except to handle DB transaction.
    """
    @functools.wraps(handler)
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except APIError as e:
            db.conn.session.rollback()
            log.error(f'{e}')
            return f'API error {e}', API_ERROR_CODE
        except schematics.exceptions.BaseError as e:
            db.conn.session.rollback()
            messages = []
            for field in e.errors:
                error_messsage = str(e.errors[field]).replace('Rogue', 'Unknown')
                messages.append(f'{field} - {error_messsage}')
            log.error(f'Model validation error: {e}')
            return f'Wrong request parameters: {", ".join(messages)}', API_ERROR_CODE
        except TypeError as e:
            db.conn.session.rollback()
            missing_args = re.match(r"(.+)missing \d+ required positional argument(s)?: (.+)", str(e))
            if missing_args:
                return f'Missing arguments: {missing_args.group(3)}', API_ERROR_CODE
            log.error(f'{e}, {repr(traceback.format_exc())}')
            return 'Server internal error', UNHANDLED_EXC_CODE
        except Exception as e:
            db.conn.session.rollback()
            log.error(f'{e}, {repr(traceback.format_exc())}')
            return 'Server internal error', UNHANDLED_EXC_CODE
        finally:
            db.conn.session.close()
    return wrapper


def api_result(handler):
    """
    Decorator to format api handler result.
    Expects from handler tuple with result object and optional code (default 200).
    Formats result as tuple (<result object>, <http result code>)
    """
    @functools.wraps(handler)
    def wrapper(*args, **kwargs):
        result = handler(*args, **kwargs)
        if isinstance(result, tuple):
            code = result[1]
            result = result[0]
        else:
            code = SUCCESS_CODE
        return result, code
    wrapper.__signature__ = inspect.signature(handler)  # preserve initial function signature
    return wrapper


def token_to_auth_user(handler):
    """
    Creates auth_user parameter from token
    """
    @functools.wraps(handler)  # preserve initial function signature
    def wrapper(*args, **kwargs):
        if not kwargs['auth_token']:
            log.debug('No or wrong user token in request')
            return 'No or wrong user token in request', NO_TOKEN_CODE
        kwargs.update({'auth_user': AuthUser(kwargs['auth_token'])})
        del kwargs['auth_token']
        return handler(*args, **kwargs)
    return wrapper
