import os

env = os.environ

PUBLIC_WEB_BASE_URL = env['PUBLIC_WEB_BASE_URL'] if 'PUBLIC_WEB_BASE_URL' in env else ''

# DB
DB_HOST = env['DB_HOST'] if 'DB_HOST' in env else ''
DB_PORT = env['DB_PORT'] if 'DB_PORT' in env else 3306
DB_USER = env['DB_USER'] if 'DB_USER' in env else ''
DB_PWD = env['DB_PWD'] if 'DB_PWD' in env else ''
DB_NAME = env['DB_NAME'] if 'DB_NAME' in env else ''
DB_CONN_MAX_AGE = int(env['DB_CONN_MAX_AGE']) if 'DB_CONN_MAX_AGE' in env else 0
DB_CHARSET = env['DB_CHARSET'] if 'DB_CHARSET' in env else 'utf8mb4'


# DOMAIN
API_DOMAIN = env['API_DOMAIN'] if 'API_DOMAIN' in env else 'naturitashome.herokuapp.com'

# APP
SUPERADMIN_EMAIL = env['SUPERADMIN_EMAIL'] if 'SUPERADMIN_EMAIL' in env else ''
SUPERADMIN_PASSWORD = env['SUPERADMIN_PASSWORD'] if 'SUPERADMIN_PASSWORD' in env else ''