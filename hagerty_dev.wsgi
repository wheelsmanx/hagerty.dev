#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/hagerty_dev/")

from hagerty_dev import app as application
application.secret_key = 'Add your secret key'
