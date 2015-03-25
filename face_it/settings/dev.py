from .base import *

DEBUG = True

try:
	from .local import *
except ImportError:
	pass

SOCIAL_AUTH_YAMMER_KEY = ''
SOCIAL_AUTH_YAMMER_SECRET = ''
