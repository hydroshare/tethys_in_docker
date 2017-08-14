"""
********************************************************************************
* Name: tethys_apps/__init__.py
* Author: Nathan Swain
* Created On: 2014
* Copyright: (c) Brigham Young University 2014
* License: BSD 2-Clause
********************************************************************************
"""
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']


import logging
import warnings

# Load the custom app config
default_app_config = 'tethys_apps.apps.TethysAppsConfig'

# Configure logging
tethys_log = logging.getLogger('tethys')
default_log_format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
default_log_handler = logging.StreamHandler()
default_log_handler.setFormatter(default_log_format)
tethys_log.addHandler(default_log_handler)
logging.captureWarnings(True)
warnings.filterwarnings(action='always', category=DeprecationWarning)




