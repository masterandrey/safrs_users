[![Build Status](https://travis-ci.org/masterandrey/api-db-prototype.png)](https://travis-ci.org/masterandrey/api-db-prototype)
[![Test coverage](https://coveralls.io/repos/github/masterandrey/api-db-prototype/badge.svg?branch=master)](https://coveralls.io/github/masterandrey/api-db-prototype?branch=master)
# Prototype for API server

Implements API server with different frameworks
* Transmute
* Swagger codegen (connexion)
* Pure flask

## Folder overview
* `create_keys.sh` - to create key and sertificate in `secret/`
* `db_migration.sh` - creates migration script in `alembic/versions/`
* `db_show_migration_sql.sh` - shows migration script as SQL
* `db_upgrade.sh` - runs migrations from `alembic/versions/`
* `dev.sh` - to run backend on local Python in Linux
* `load.sh` - to run load tests (URL in `load.yaml`)
* `markup.sh` - converts swagger API into confluence wiki compatible markdown
* `prod.sh` - to run backend on AWS
* `psql.sh` - to run postgres CLI
* `test.sh` - run tests (you can use `-k` or `-m` to filter them by name or by mark respectively)
* `smoke_test.sh` - quick curl test (request JWT and after that user list with it)
* `api` - swagger (Open API) description of the API served by the backend
* `alembic` - DB metadata versioning
* `src/controllers` - application logic
* `src/db` - SQLAlchemy models
* `src/flask_server` - HTTP server (request routing to application logic)
* `src/transmute_server` - Transmute version
* `src/swagger_server` - Connexion version (swagger codegen)
* `src/secret` - key and sertificate for signing and verification of secutiry tokens (`jwt_token.py`)
* `src/tests` - py.test tests, call test.sh to run them
* `src/app.py` - WSGI app (for Flask, uWsgi, Unicorn etc)
* `src/journaling.py` - Central journaling settings
* `src/jwt_token.py` - Security tokens crypto
* `src/passwords.py` - Password hashing crypto
* `src/settings.py` - Configs for test/dev/prod

Libraries:
* swagger doc auto generation [transmute](https://github.com/toumorokoshi/flask-transmute)
* DB [SQLAlchemy](http://wiki.python.su/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8/SQLAlchemy)
* [alembic](https://pypi.org/project/alembic/) for DB metadata versioning
* flask
* [flask-login](https://flask-login.readthedocs.io/en/latest/)
* [jwt](https://realpython.com/token-based-authentication-with-flask/)

To create objects in empty DB use `db_create.sh`.
The DB connect string is in `src/config.py`.

For `transmute_server` flavor of the app, API description generated as 
`localhost:5000/swagger` (see `api_doc.sh`).

### Open API (swagger)
You can convert the swagger file `api/swagger.yaml` into document at 
`editor.swagger.io` or `Amazon AWS API Gateway`.


### Configs

See `settings.py`.

For `Prod` config you should specify DB in `settings.py`.
This config would be used by default (if no `FLASK_ENV` specified).

### Deployment

To run dev version `server$ FLASK_ENV=development python3.7 app.py`.

In production you should use something like 
[Gunicorn or uWsgi](http://flask.pocoo.org/docs/1.0/deploying/).

See example in `prod.sh` and `Dockerfile`.

## Security
In developer version automatically created user with email `admin@` 
and password `admin`.

### JWT keys

For web token crypto server uses keys from files configured in the config 
object.
Default is `sever/security` folder.

Example how to recreate keys see in `create_keys.sh`.
Private key is for token issuing. 

If the web application would get tockens from external service
like Amazon Cognito, you should provide only public key from that 
external service, so our server could check this external service's tokens.

Public key is expected in `pem` certificate format. 
