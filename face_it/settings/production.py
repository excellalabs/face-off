from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(default='postgres://waxqvtkhzjuakg:6M5hafAUkFzrgEz2KCjBT065Ih@ec2-107-22-253-198.compute-1.amazonaws.com:5432/d93akfi9778vpr')}

try:
	from .local import *
except ImportError:
	pass


SOCIAL_AUTH_YAMMER_KEY = 'O1J0JxLC38lOOVvaCIAWcQ'
SOCIAL_AUTH_YAMMER_SECRET = 'gMSJjpZYcrZKfLmHTjRPyZpVK3Z5bIeXv5nRqMOuV4'
