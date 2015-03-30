from .base import *
import dj_database_url

DEBUG = False

try:
	from .local import *
except ImportError:
	pass


ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}

SOCIAL_AUTH_YAMMER_KEY = os.environ.get('SOCIAL_AUTH_YAMMER_KEY')
SOCIAL_AUTH_YAMMER_SECRET = os.environ.get('SOCIAL_AUTH_YAMMER_SECRET')

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']