from os import getenv

user = getenv('MAINPORTFOLIO_USER')
password = getenv('MAINPORTFOLIO_PWD')
database = getenv('MAINPORTFOLIO_DB')
host = getenv('MAINPORTFOLIO_HOST')

SECRET_KEY = "THTD673&?/YHG/@H393_YEU"
ADMIN_EMAIL = "admin@personal.com"
USER_PROFILE_PATH = "myport/static/assets/images/profile/"
SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'carryoby@gmail.com'
MAIL_PASSWORD = 'uxjq wcqv yntk dwju'
MAIL_USE_SSL = True
