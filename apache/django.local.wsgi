import os, sys
sys.path.append('/var/www/vmserver')
os.environ['DJANGO_SETTINGS_MODULE'] = 'meaninglesscodename.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
