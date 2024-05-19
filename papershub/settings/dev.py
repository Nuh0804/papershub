from .common import *
import os

DEBUG = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]

SECRET_KEY = os.getenv("DEV_SECRET")

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('DB_NAME'),
       'HOST': 'localhost',
       'USER': os.getenv('DB_USER'),
       'PASSWORD': os.getenv('DB_PASS'),
       'PORT': '5432'
   }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_HOST = os.getenv("MAILSENDER_SMTP_SERVER")
EMAIL_HOST_USER = os.getenv("MAILSENDER_SMTP_USERNAME")
EMAIL_HOST_PASSWORD = os.getenv("MAILSENDER_SMTP_PASSWORD")
EMAIL_PORT = os.getenv("MAILSENDER_SMTP_PORT")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True

DOMAIN = ("localhost:3000") #local: localhost:3000
SITE_NAME = ('localhost:3000')