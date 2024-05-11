from .common import *

DEBUG = True

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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True