import os

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres@localhost:5432/django-prices-vatlayer',
        conn_max_age=600)
}

SECRET_KEY = 'irrelevant'
INSTALLED_APPS = [
    'django_prices_vatlayer',
]


VATLAYER_ACCESS_KEY = os.environ.get('VATLAYER_ACCESS_KEY', '')
