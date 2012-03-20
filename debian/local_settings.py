# This file is deployed by APT and not recommended to be modified manually.
# Instead, add a /etc/scrapyorh/server_settings.py file for your custom
# settings.

import socket

DEBUG = False

MAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[scrapyorh] '
SERVER_EMAIL = 'scrapyorh@%s' % socket.getfqdn()
ADMINS = [('Errors', 'errors@scrapinghub.com')]

# scrapyorg doesn't require a database (yet)
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = '/var/lib/scrapyorh/scrapyorh.db'
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''

TEMPLATE_DIRS = ['/usr/share/scrapyorh/templates']
MEDIA_ROOT = '/usr/share/scrapyorg/static'

try:
    from server_settings import *
except ImportError:
    pass
