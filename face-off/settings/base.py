# Django settings for face-off project.

import os, sys, urlparse

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')

# Modify sys.path to include the lib directory
sys.path.append(os.path.join(PROJECT_ROOT, "lib"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PIPELINE_ENABLED = True


EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = (
)

if 'test' in sys.argv or 'testserver' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # path to collab sqlite3 database file
            'NAME': '',
            'USER': '',      # leave empty
            'PASSWORD': '',  # leave empty
            'HOST': '',      # leave empty
            'PORT': '',      # leave empty
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'face-off',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '',  # Set to empty string for localhost.
            'PORT': '',  # Set to empty string for default.
            'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Bower Configuration
BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'core/static')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
    'pipeline.finders.PipelineFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = STATIC_URL + 'media/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

# CSS Files. Eventually remove CDN TODO
PIPELINE_CSS = {
    # Project libraries.
    'css': {
        'source_filenames': (
            'bower_components/bootstrap-social/bootstrap-social.css',
            'bower_components/font-awesome/css/font-awesome.css',
            'css/*.css',
        ),
        # Compress passed libraries and have
        # the output in`css/css.min.css`.
        'output_filename': 'css/css.min.css',
        'variant': 'datauri',
    }
    # ...
}
# JavaScript files.
PIPELINE_JS = {
    # Project JavaScript libraries.
    'js': {
        'source_filenames': (
            'bower_components/underscore/underscore.js',
            'js/loadLast/*.js',
        ),
        # Compress all passed files into `js/js.min.js`.
        'output_filename': 'js/js.min.js',
    },
    # ...
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-_9f3*2^6vul3^qz^x+(s^w8ko(4k#v!ftkji8fq+&=@^%xh^8'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
    'face-off.context_processors.global_suggestion_form',
    'face-off.context_processors.yammer_client_id',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.yammer.YammerOAuth2',
    'core.custom_authenticate.UserProfileAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'face-off.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'face-off.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'debug_toolbar',
    'suit',
    'django.contrib.admin',
    # 'django.contrib.sites',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'core',
    'social.apps.django_app.default',
    'djangobower',
    'pipeline',
    'face-off',
    'import_export',
    'storages',
    's3direct',
    'crispy_forms',
)

EMAIL_SUBJECT_PREFIX = '[face-off] '

LOGIN_REDIRECT_URL = '/'

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# django-debug-toolbar settings
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_URL = '/login'

redis_url = os.environ.get('REDISTOGO_URL', 'redis://127.0.0.1:6379/1')

# Cache Backend
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s" % redis_url,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,  # Redis is only used for cache so we do not want exceptions when Redis is down
        }
    }
}

# Custom User Creation
AUTH_USER_MODEL = 'core.UserProfile'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'core.user_pipeline.post_user_creation',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# Django Suit configuration
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Col-league Administration',

    'MENU_EXCLUDE': ('auth.group', 'auth'),
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
}

#Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# S3 Configuration
try:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
except KeyError:
    print 'Set up AWS Global Variables'
    pass

S3DIRECT_ENDPOINT = 'colleague-bucket.s3.amazonaws.com'
S3DIRECT_REGION = 'us-east-1'
# Destinations in the following format:
# {destination_key: (path_or_function, auth_test, [allowed_mime_types], permissions, custom_bucket)}
#
# 'destination_key' is the key to use for the 'dest' attribute on your widget or model field
S3DIRECT_DESTINATIONS = {
    # Allow anybody to upload jpeg's and png's.
    'imgs': ('uploads/profile-images', lambda u: True, ['image/jpeg', 'image/png'],),
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
