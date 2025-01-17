from pathlib import Path
from corsheaders.defaults import default_headers
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-e)rv!#2)=0+_8*nc@eav9$n1n7$*u=vy+jpsfr1a99@ix@*tls'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
# Secret Key
SECRET_KEY = config('SECRET_KEY')

# Debug Mode
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = ['127.0.0.1','https://react-stater.vercel.app/', 'localhost','mesumandahal.pythonanywhere.com']

# Frontend URL
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:5173')

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'users',
    'drf_spectacular',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add this line
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#my added package setting

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}

AUTH_USER_MODEL = 'users.CustomUser'

DJOSER = {
    'USER_ID_FIELD': 'email',  # Use email as the unique identifier
    'LOGIN_FIELD': 'email',  # Specify email as the login field
    'SET_PASSWORD_RETYPE': True,  # Requires re_new_password for confirmation
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,  # Sends confirmation email after password change
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'http://192.168.1.105:5173/password/reset/confirm/{uid}/{token}',
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    "EMAIL": {
        #"password_reset": "djoser.email.PasswordResetEmail",
        "password_reset": "users.emails.CustomPasswordResetEmail",
        "activation": "users.emails.CustomAccountActivationEmail",
    },
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
    },
}


# URL to access static files in the browser
STATIC_URL = '/static/'

# Directory where `collectstatic` will collect static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Optional: Directories for additional static files (if any)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

CORS_ALLOWED_ORIGINS = [
    "http://192.168.1.105:5173",  # Replace with your React app's URL
    "http://localhost:5173",
    "https://react-stater.vercel.app"
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFTOKEN',  # Explicitly allow this header
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://192.168.1.105:5173",
    "https://react-stater.vercel.app/",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}