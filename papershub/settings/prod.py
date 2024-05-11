import os
import dj_database_url

from .common import *

DEBUG = False

CORS_ALLOWED_ORIGINS = [
    "papershub.co.tz",
    "https://papershub.co.tz",
]

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['papershub-prod-ee9f6b8e1268.herokuapp.com']

DATABASES = {
   'default': dj_database_url.config()
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ["MAILGUN_SMTP_PORT"]
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True