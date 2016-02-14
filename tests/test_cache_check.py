from __future__ import absolute_import

import os
import shutil
import unittest

from openross import engine
from openross.pipeline.cache_check import CacheCheck
from tests import test_settings


class TestCacheCheck(unittest.TestCase):

    def setUp(self):
        if not os.path.exists(test_settings.CACHE_LOCATION):
            os.makedirs(test_settings.CACHE_LOCATION)

        self.testfile_original = os.path.join(
            test_settings.CACHE_LOCATION, 'image.jpeg'
        )
        open(self.testfile_original, 'a').close()

    def tearDown(self):
        if os.path.exists(test_settings.CACHE_LOCATION):
            shutil.rmtree(test_settings.CACHE_LOCATION)

    def test_cache_has_original_image(self):
        cachec = CacheCheck(engine.BobRossEngine())
        from openross import settings
        settings.CACHE_LOCATION = test_settings.CACHE_LOCATION

        test_file_path = os.path.join(test_settings.CACHE_LOCATION, 'image*')
        cache_file_path = cachec._find_cache_matches(test_file_path)
        self.assertEqual(cache_file_path, self.testfile_original)

        test_file_path = os.path.join(test_settings.CACHE_LOCATION, 'image2*')
        cache_file_path = cachec._find_cache_matches(test_file_path)
        self.assertEqual(cache_file_path, False)
