# This file is deployed by APT and not recommended to be modified manually.
# Instead, add a /etc/scrapyorg/server_settings.py file for your custom
# settings.

import socket

DEBUG = False

MAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[scrapyorg] '
SERVER_EMAIL = 'scrapyorg@%s' % socket.getfqdn()
ADMINS = [('Errors', 'errors@scrapinghub.com')]

# scrapyorg doesn't require a database (yet)
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = '/var/lib/scrapyorg/scrapyorg.db'
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''

TEMPLATE_DIRS = ['/usr/share/scrapyorg/templates']
MEDIA_ROOT = '/usr/share/scrapyorg/static'

try:
    from server_settings import *
except ImportError:
    pass
