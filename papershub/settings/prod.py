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

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUD_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_API_KEY"),
    'API_SECRET': os.getenv("CLOUDINARY_SECRET"),
}