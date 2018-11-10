import db.conn
import db.models
from controllers.models import NewUser


def create_user(new_user: NewUser):
    """
    Creates user.
    Returns new user id.
    """
    try:
        # todo: check uniq name, email?
        db_user = db.models.User(**new_user.as_dict)
        db.conn.session.add(db_user)
        db.conn.session.commit()
        return {
            'result': {'id': db_user.id},
            'success': True
        }
    except Exception as e:
        db.conn.session.rollback()
        return f'{e}', 400  #todo: internal exception only to log