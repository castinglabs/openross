from __future__ import absolute_import, print_function, unicode_literals

import os
import shutil

from twisted.internet import defer
from twisted.trial import unittest

from openross import engine
from openross.pipeline.cacher import Cacher
from tests import test_settings


class TestCacher(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(test_settings.CACHE_LOCATION):
            os.makedirs(test_settings.CACHE_LOCATION)

        self.testpayload = {
            'width': '200',
            'height': '200',
            'mode': 'resize',
            'image_path': 'test.jpeg',
            'image': 'test',
            'original_image': 'test',
        }
        self.testlocation = os.path.join(
            test_settings.CACHE_LOCATION, 'test_200x200_resize.jpeg'
        )

        self.testpayload_original = {
            'width': '-1',
            'height': '-1',
            'mode': 'r',
            'image_path': 'test.jpeg',
            'image': 'test',
            'original_image': 'test',
            'skip_resize': True,
        }
        self.testlocation_original = os.path.join(
            test_settings.CACHE_LOCATION, 'test.jpeg'
        )

    def tearDown(self):
        if os.path.exists(test_settings.CACHE_LOCATION):
            shutil.rmtree(test_settings.CACHE_LOCATION)

    @defer.inlineCallbacks
    def test_cache_write_normal(self):
        """ Test cacher pipeline for normal file
        """
        cacher = Cacher(engine.BobRossEngine())
        from openross import settings
        settings.CACHE_LOCATION = test_settings.CACHE_LOCATION + '/'

        yield cacher.process_image(self.testpayload)
        self.assertTrue(os.path.exists(self.testlocation), True)

    @defer.inlineCallbacks
    def test_cache_write_original(self):
        """ Test cacher pipeline for normal file
        """
        cacher = Cacher(engine.BobRossEngine())
        from openross import settings
        settings.CACHE_LOCATION = test_settings.CACHE_LOCATION + '/'

        yield cacher.process_image(self.testpayload_original)
        self.assertTrue(os.path.exists(self.testlocation_original), True)
