import os
from beautifulcat.settings import BASE_DIR

SECRET_KEY = 'TOKEN'

# Never deploy a site into production with DEBUG turned on.
# It change to True (strictly for development only).
# Also it settings make your django static files access fail


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beautifulcat',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}