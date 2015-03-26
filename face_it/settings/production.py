from .base import *
import dj_database_url

try:
	from .local import *
except ImportError:
	pass

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}

SOCIAL_AUTH_YAMMER_KEY = os.environ.get('SOCIAL_AUTH_YAMMER_KEY')
SOCIAL_AUTH_YAMMER_SECRET = os.environ.get('SOCIAL_AUTH_YAMMER_SECRET')
