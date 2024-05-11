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