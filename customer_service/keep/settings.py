from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q%a0w=pvla5nj1yq_1vtzz@0tb#dr(f4c5+7nl-ipq%7)-0f6f'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'customers',
    'orders',
    "django_apscheduler",
    'django_saml2_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

ROOT_URLCONF = 'keep.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'keep.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'customerapp',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'customerapp-mysql',
        'PORT': 3306,
    }
}


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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    #'METADATA_AUTO_CONF_URL': 'https://app.onelogin.com/saml/metadata/bcd6fdc6-7221-4798-b20b-5b6569a3bfc7',
    'METADATA_LOCAL_FILE_PATH': 'MIID7jCCAtagAwIBAgIUFTc+S0weFAP/oFZV9cWxH+Up1EIwDQYJKoZIhvcNAQEFBQAwSzEWMBQGA1UECgwNS2VlcCBTaXN0ZW1hczEVMBMGA1UECwwMT25lTG9naW4gSWRQMRowGAYDVQQDDBFPbmVMb2dpbiBBY2NvdW50IDAeFw0yMTA3MTcxODA2MjFaFw0yNjA3MTcxODA2MjFaMEsxFjAUBgNVBAoMDUtlZXAgU2lzdGVtYXMxFTATBgNVBAsMDE9uZUxvZ2luIElkUDEaMBgGA1UEAwwRT25lTG9naW4gQWNjb3VudCAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQbUKLmVagzpWrU0LLfd1B8qZmPsmeZPvHntDRTldgMVlzTQ6uyhGcSeiG9hRS/6iExkdifx5Pqi0azWzaLCnKJH1S3rxuiw7z/jTP5aAnMbJUl0P+KwfXDv8RbhMgX6fT0BZu+Cm8M2QIb6MzY/PTsxa5r2JJCjpnX28LoZxxaDbB8PlpoHn0HRwwz0DbIfEgfV3eN9E+/KuL7S/vr4IpIWdROD1gfyZFovUI5WhxveB3AnXSmlhebsxooEUTnctb5ryGzr9VwCrcsYsayTBgO8Pf+2XnmY/4w6icD+E0iAmguErwyxk4UDkQxVfFc06mdeBn+vx0Hd1a/vl1fm0pAgMBAAGjgckwgcYwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQULgpo/P+piYgoX0DIIidYuRXI4GowgYYGA1UdIwR/MH2AFC4KaPz/qYmIKF9AyCInWLkVyOBqoU+kTTBLMRYwFAYDVQQKDA1LZWVwIFNpc3RlbWFzMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxGjAYBgNVBAMMEU9uZUxvZ2luIEFjY291bnQgghQVNz5LTB4UA/+gVlX1xbEf5SnUQjAOBgNVHQ8BAf8EBAMCB4AwDQYJKoZIhvcNAQEFBQADggEBAMK+MAAJvUIFm11zV6TjXJsE1dLqM2IIGwUczMBXULdgrtQTKOtlXTXQ+ItTtIC2+0sbMWVyUt0h9MJfN/PY3QQtBFnei0EglcDg0TagwfQHH3XoAccl8R67fGtaESw0mWxkmAmtR6IIB7DPfu1oA8D044Gcombe2omttvgAHA5c/NLxQ4JWwvlGRYuppFas07xK2r5Ti+/IIEUaMaaJPw/WO0Ybyhb1nXshb3r9XHFqmcpW6+ZcGyzJzgDct0bPktCbfQPc4TLD0gZEf66jGGCg3iN3A7Aa+gBCP0zQWjHAUptOu+WLNppgT89BrGoR5VT+L9WOGwmDsHb+Ivd+14E=',
    # Optional settings below
    'DEFAULT_NEXT_URL': '/admin',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': True,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'Email',
        'username': 'UserName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
    },
    
    'ASSERTION_URL': 'https://BACKEND.example.com',
    'ENTITY_ID': 'https://BACKEND.example.com.com/sso/acs/',
    'NAME_ID_FORMAT': 'FormatString', # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'https://myfrontendclient.com', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}
