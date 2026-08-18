import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")

# Security key used for cryptographic signing
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-in-production")

# Run in debug mode if the environment variable is set to 'true'
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# Hostnames that this Django site can serve
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1,testserver").split(",") if h.strip()]

# Applications enabled for this Django instance
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
]

# Pipeline of components executed during response handling
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# The Python path to the root URL configurations
ROOT_URLCONF = "urls"

# Configuration for template rendering engines
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# The entry point for WSGI-compatible web servers
WSGI_APPLICATION = "project.wsgi.application"

# Database connection settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "CONN_MAX_AGE": 60,
        "ATOMIC_REQUESTS": True,
    }
}

# To use MySQL instead of SQLite, uncomment the following and comment out the above:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("DB_NAME", "writing_feedback"),
#         "USER": os.getenv("DB_USER", "root"),
#         "PASSWORD": os.getenv("DB_PASSWORD", ""),
#         "HOST": os.getenv("DB_HOST", "localhost"),
#         "PORT": os.getenv("DB_PORT", "3306"),
#         "CONN_MAX_AGE": 60,
#         "ATOMIC_REQUESTS": True,
#         "OPTIONS": {
#             "charset": "utf8mb4",
#             "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Email sending configurations
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "true").lower() == "true"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "false").lower() == "true"
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", "10"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER or "webmaster@localhost")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Fall back to printing emails to the terminal if SMTP credentials aren't set
if not EMAIL_HOST or not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# URL route to redirect users to when login is required
LOGIN_URL = "login"

# List of password validation rules
AUTH_PASSWORD_VALIDATORS = []

# Localization and time zone configurations
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# User-uploaded files configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type for auto-generated model IDs
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
