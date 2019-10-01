SECRET_KEY = '__SECRET_KEY__'

ADMINS = (
     ('Mailman Suite Admin', 'root@__DOMAIN__'),
)

ALLOWED_HOSTS = ['*']

MAILMAN_REST_API_URL = 'http://localhost:__PORT_WEB__'
MAILMAN_REST_API_USER = '__REST_API_ADMIN_USER__'
MAILMAN_REST_API_PASS = '__REST_API_ADMIN_PWD__'
MAILMAN_ARCHIVER_KEY = '__ARCHIVER_KEY__'
MAILMAN_ARCHIVER_FROM = ('127.0.0.1', '::1', '__DOMAIN_IP__')

INSTALLED_APPS = (
    'hyperkitty',
    'postorius',
    'django_mailman3',
    'django.contrib.admin',
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
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
        },
    }
}


USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_SCHEME', 'https')
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    "archives/api/mailman/.*",
]
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAILNAME = '__DOMAIN__'
DEFAULT_FROM_EMAIL = 'postorius@{}'.format(EMAILNAME)
SERVER_EMAIL = 'root@{}'.format(EMAILNAME)

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

SOCIALACCOUNT_PROVIDERS = {
}

COMPRESS_OFFLINE = True

POSTORIUS_TEMPLATE_BASE_URL = 'https://__DOMAIN__'
