# This file is imported by the Mailman Suite. It is used to override
# the default settings from /usr/share/mailman3-web/settings.py.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__SECRET_KEY__'

ADMINS = (
     ('Mailman Suite Admin', 'root@__DOMAIN__'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
# Set to '*' per default in the Deian package to allow all hostnames. Mailman3
# is meant to run behind a webserver reverse proxy anyway.
ALLOWED_HOSTS = [
    #"localhost",  # Archiving API from Mailman, keep it.
    # "lists.your-domain.org",
    # Add here all production URLs you may have.
    '*'
]

# Mailman API credentials
MAILMAN_REST_API_URL = 'http://localhost:__PORT__'
MAILMAN_REST_API_USER = '__REST_API_ADMIN_USER__'
MAILMAN_REST_API_PASS = '__REST_API_ADMIN_PWD__'
MAILMAN_ARCHIVER_KEY = '__ARCHIVER_KEY__'
MAILMAN_ARCHIVER_FROM = ('127.0.0.1', '::1')

# Application definition

INSTALLED_APPS = (
    'hyperkitty',
    'postorius',
    'django_mailman3',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_mailman3.lib.auth.fedora',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.gitlab',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.stackexchange',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # Use 'sqlite3', 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'ENGINE': 'django.db.backends.mysql',
        # DB name or path to database file if using sqlite3.
        'NAME': '__DB_NAME_WEB__',
        # The following settings are not used with sqlite3:
        'USER': '__DB_USER_WEB__',
        'PASSWORD': '__DB_PWD_WEB__',
        # HOST: empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # PORT: set to empty string for default.
        'PORT': '',
        # OPTIONS: Extra parameters to use when connecting to the database.
        'OPTIONS': {
            # Set sql_mode to 'STRICT_TRANS_TABLES' for MySQL. See
            # https://docs.djangoproject.com/en/1.11/ref/
            #     databases/#setting-sql-mode
            #'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# If you're behind a proxy, use the X-Forwarded-Host header
# See https://docs.djangoproject.com/en/1.8/ref/settings/#use-x-forwarded-host
USE_X_FORWARDED_HOST = True

# And if your proxy does your SSL encoding for you, set SECURE_PROXY_SSL_HEADER
# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_SCHEME', 'https')

# Other security settings
SECURE_SSL_REDIRECT = True
# If you set SECURE_SSL_REDIRECT to True, make sure the SECURE_REDIRECT_EXEMPT
# contains at least this line:
SECURE_REDIRECT_EXEMPT = [
    "archives/api/mailman/.*",
]
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Set default domain for email addresses.
EMAILNAME = '__DOMAIN__'

# If you enable internal authentication, this is the address that the emails
# will appear to be coming from. Make sure you set a valid domain name,
# otherwise the emails may get rejected.
# https://docs.djangoproject.com/en/1.8/ref/settings/#default-from-email
# DEFAULT_FROM_EMAIL = "mailing-lists@you-domain.org"
DEFAULT_FROM_EMAIL = 'root@{}'.format(EMAILNAME)

# If you enable email reporting for error messages, this is where those emails
# will appear to be coming from. Make sure you set a valid domain name,
# otherwise the emails may get rejected.
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SERVER_EMAIL
# SERVER_EMAIL = 'root@your-domain.org'
SERVER_EMAIL = 'root@{}'.format(EMAILNAME)


# Django Allauth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"


#
# Social auth
#
SOCIALACCOUNT_PROVIDERS = {
    #'openid': {
    #    'SERVERS': [
    #        dict(id='yahoo',
    #             name='Yahoo',
    #             openid_url='http://me.yahoo.com'),
    #    ],
    #},
    #'google': {
    #    'SCOPE': ['profile', 'email'],
    #    'AUTH_PARAMS': {'access_type': 'online'},
    #},
    #'facebook': {
    #   'METHOD': 'oauth2',
    #   'SCOPE': ['email'],
    #   'FIELDS': [
    #       'email',
    #       'name',
    #       'first_name',
    #       'last_name',
    #       'locale',
    #       'timezone',
    #       ],
    #   'VERSION': 'v2.4',
    #},
}

# On a production setup, setting COMPRESS_OFFLINE to True will bring a
# significant performance improvement, as CSS files will not need to be
# recompiled on each requests. It means running an additional "compress"
# management command after each code upgrade.
# http://django-compressor.readthedocs.io/en/latest/usage/#offline-compression
COMPRESS_OFFLINE = True

POSTORIUS_TEMPLATE_BASE_URL = 'https://__DOMAIN__'
