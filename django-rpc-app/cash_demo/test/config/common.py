import os
import string
import datetime
from os.path import join
# from distutils.util import strtobool
# from django.middleware import LocaleMiddleware

from configurations import Configuration
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    DEBUG = False
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_filters',
        # Enable sites
        # 'django.contrib.sites',
        # 'cash_demo.demo',
        'cash_user',
        'cash_demo.test',

    )
    # Define current site ID
    SITE_ID = 1

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        # New to support Accept-Language in header - Shoul before common middleware
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 'users.middleware.BoxMeSessionCheckMiddleware',  # New for check referral

    )

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = 'cash_demo.test.urls'
    SECRET_KEY = os.getenv(
        'DJANGO_SECRET_KEY', "79#=^htlif!6b1d9txjv+5c)xst)xwej@4_vw+#8g!y*tr+0(x"
    )
    WSGI_APPLICATION = 'cash_demo.test.wsgi.application'

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("MYSQL_DEFAULT_SSID", "cash_demo"),
            "USER": os.getenv("MYSQL_DEFAULT_USER", "root"),
            "PASSWORD": os.getenv("MYSQL_DEFAULT_PASSWORD", "Tungtt2019@"),
            "HOST": os.getenv("MYSQL_DEFAULT_HOST", "127.0.0.1"),
            "PORT": os.getenv("MYSQL_DEFAULT_PORT", "3306"),
            "CONN_MAX_AGE": os.getenv("CONN_MAX_AGE", 60)
        },
        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'OPTIONS': {
        #         'read_default_file': '/etc/mysql/my.cnf',
        #     },
        # }
    }

    AUTH_USER_MODEL = 'cash_user.User'
    # AUTH_USER_PROFILE_MODEL = 'users.UserProfile'

    # General
    LOCALE_PATHS = (
        'locale/',
    )

    def ugettext(s): return s
    LANGUAGES = (
        ('en', ugettext('English')),
        ('vi', ugettext('Tiếng Việt')),
    )
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True
    USE_L10N = False
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static files (CSS, JavaScript, Images)sou .
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'storage'))
    STATICFILES_DIRS = []
    LOCAL_STATIC_DIRS = '/storage/'
    # test on local
    LOCAL_STATIC_TEST = "/home/tungfit/Dropbox/internetofmoney/cash-demo/storage/"
    STATIC_URL = '/storage/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'
    # Templates
    TEMPLATES_ROOT = os.path.join(BASE_DIR, "templates")
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'DIRS': STATICFILES_DIRS,
            # 'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
            'DIRS': [TEMPLATES_ROOT],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    # [DiepDT] Custom authentication backend
    # AUTHENTICATION_BACKENDS = (
    #     # New authentication for Accounkit only
    #     'users.authentication.AccountKitAuthenticationBackend',
    #     # Needed to login by username in Django admin, regardless of `allauth`
    #     'django.contrib.auth.backends.ModelBackend',

    #     # `allauth` specific authentication methods, such as login by e-mail
    #     'allauth.account.auth_backends.AuthenticationBackend',
    # )
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    # DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    # AUTH_PASSWORD_VALIDATORS = [
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #     },
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #     },
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #     },
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #     },
    # ]

    CASH_GRPC_SERVICE_HOST = {
        "DEMO": os.getenv("CASH_GRPC_SERVICE_DEMO", "127.0.0.1:50052")
    }

    # Logging
    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'formatters': {
    #         'django.server': {
    #             '()': 'django.utils.log.ServerFormatter',
    #             'format': '[%(server_time)s] %(message)s',
    #         },
    #         'verbose': {
    #             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    #         },
    #         'simple': {
    #             'format': '%(levelname)s %(message)s'
    #         },
    #     },
    #     'filters': {
    #         'require_debug_true': {
    #             '()': 'django.utils.log.RequireDebugTrue',
    #         },
    #     },
    #     'handlers': {
    #         'django.server': {
    #             'level': 'INFO',
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'django.server',
    #         },
    #         'console': {
    #             'level': 'DEBUG',
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'simple'
    #         },
    #         'mail_admins': {
    #             'level': 'ERROR',
    #             'class': 'django.utils.log.AdminEmailHandler'
    #         },
    #         'log_request': {
    #             'level': 'INFO',
    #             'formatter': 'django.server',
    #             'class': 'logging.FileHandler',
    #             'filename': 'request.log',
    #         },
    #     },
    #     'loggers': {
    #         'django': {
    #             'handlers': ['console'],
    #             'propagate': True,
    #         },
    #         'django.server': {
    #             'handlers': ['django.server'],
    #             'level': 'INFO',
    #             'propagate': False,
    #         },
    #         'django.request': {
    #             'handlers': ['mail_admins', 'console', 'log_request'],
    #             'level': 'ERROR',
    #             'propagate': False,
    #         },
    #         'django.db.backends': {
    #             'handlers': ['console'],
    #             'level': 'INFO'
    #         },
    #     }
    # }
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.AllowAny',
            # 'cash_user.authentication.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            # 'cash_user.authentication.JWTAuthentication',
            # 'rest_framework.authentication.SessionAuthentication',
            # 'rest_framework.authentication.BasicAuthentication',
        ),
    }
    JWT_AUTH = {
        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
        'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    }
