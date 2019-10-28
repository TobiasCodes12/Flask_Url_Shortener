import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
ADMIN_USERNAME = os.environ.get('ADMIN_UNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PWD')