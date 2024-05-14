from .common import *

DEBUG = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]

SECRET_KEY = 'django-insecure-nd)e03wmz1ze@rq$4hz_lo^%utqm_%_2$ruv3v7yl%mjhlf56v'

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'papershub',
       'HOST': 'localhost',
       'USER': 'postgres',
       'PASSWORD': 'nuhusaidi',
       'PORT': '5432'
   }
}

