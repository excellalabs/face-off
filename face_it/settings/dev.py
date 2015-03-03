from .base import *

DEBUG = True

try:
	from .local import *
except ImportError:
	pass

SOCIAL_AUTH_YAMMER_KEY = 'OCnfR7VJNBbcSS8GXMCi3A'
SOCIAL_AUTH_YAMMER_SECRET = 'y1MZSoo0MuX8RJPEjMbZWJDvafR9mZmFWWUfHOcZgxM'
