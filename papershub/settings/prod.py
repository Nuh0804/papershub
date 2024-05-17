import os
import dj_database_url
from .common import *

DEBUG = False

CORS_ALLOWED_ORIGINS = [
    "https://papershub.co.tz",
]

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['papershub-prod-ee9f6b8e1268.herokuapp.com']

DATABASES = {
   'default': dj_database_url.config()
}

#media file conf
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


#email conf
EMAIL_HOST = os.environ.get('MAILSENDER_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('MAILSENDER_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MAILSENDER_SMTP_PASSWORD')
EMAIL_PORT = os.environ.get("MAILSENDER_SMTP_PORT")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True