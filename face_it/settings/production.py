from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

try:
	from .local import *
except ImportError:
	pass


SOCIAL_AUTH_YAMMER_KEY = 'R97DK2ADollIPpQZz4eeA'
SOCIAL_AUTH_YAMMER_SECRET = 'lLtRosuTAso9PQWDojdrhWtSvNk2UZIGbAREjhT2Qg'
