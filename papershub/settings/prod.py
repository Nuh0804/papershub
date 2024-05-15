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

