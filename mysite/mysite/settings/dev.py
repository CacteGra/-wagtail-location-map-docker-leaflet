from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@ep+xn2(b0+k2e$9kb((w_#f_!=^gzeh4whzuh(vzr@94o#j!a"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('POSTGRES_DB', 'db.sqlite3'),
        'USER': os.environ.get('POSTGRES_USER', 'dbuser'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'dbpasswd'),
        'HOST': 'db',
        'PORT': '5433',
    }
}
#WAGTAILADMIN_BASE_URL = '127.0.0.1'

try:
    from .local import *
except ImportError:
    pass
