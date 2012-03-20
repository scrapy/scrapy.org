import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'scrapyorg.settings'
sys.path.append('/etc/scrapyorg')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
