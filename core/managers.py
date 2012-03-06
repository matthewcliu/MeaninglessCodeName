from django.db import models
from django.db.models import Q, Count
from django.db import transaction
from django.contrib.auth.models import User

from meaninglesscodename import settings
#from wedding.core.lib import facebook

import Image
import os
import MySQLdb
import logging
import shutil
import time
import string
import urllib2

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = '/tmp/debug.log',
    filemode = 'w'
)

"""
Insert Model Managers Here
"""