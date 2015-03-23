from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(default='postgres://postgres:@localhost:5432/db')}

try:
	from .local import *
except ImportError:
	pass


SOCIAL_AUTH_YAMMER_KEY = 'R97DK2ADollIPpQZz4eeA'
SOCIAL_AUTH_YAMMER_SECRET = 'lLtRosuTAso9PQWDojdrhWtSvNk2UZIGbAREjhT2Qg'
