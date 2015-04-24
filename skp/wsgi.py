import os
import sys

sys.path = [' /var/www/skp'] + sys.path
os.environ["DJANGO_SETTINGS_MODULE"]= "skp.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
