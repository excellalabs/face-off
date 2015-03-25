from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(default=os.environ.get('HEROKU_PSTGRS_URL'))}

try:
	from .local import *
except ImportError:
	pass


SOCIAL_AUTH_YAMMER_KEY = os.environ.get('SOCIAL_AUTH_YAMMER_KEY')
SOCIAL_AUTH_YAMMER_SECRET = os.environ.get('SOCIAL_AUTH_YAMMER_SECRET')
