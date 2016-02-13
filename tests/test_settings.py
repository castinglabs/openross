from __future__ import absolute_import, print_function, unicode_literals

import os

from openross.settings import *  # noqa


TEST = True
TEST_DATA_DIR = os.path.abspath(os.path.join('tests', 'test_data'))
CACHE_LOCATION = os.path.join(TEST_DATA_DIR, 'cache')
