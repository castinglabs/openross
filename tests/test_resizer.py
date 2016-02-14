from __future__ import absolute_import

import hashlib
import os
import unittest

from openross import engine
from openross.pipeline.resizer import Resizer
from tests import test_settings


class TestResizer(unittest.TestCase):
    def setUp(self):
        self.test_in = os.path.join(
            test_settings.TEST_DATA_DIR, 'resizer', 'test-in.jpeg'
        )
        self.test_reference_crop = os.path.join(
            test_settings.TEST_DATA_DIR, 'resizer', 'test-reference-crop.jpeg'
        )
        self.test_reference_resize = os.path.join(
            test_settings.TEST_DATA_DIR, 'resizer',
            'test-reference-resize.jpeg'
        )
        self.test_reference_resizecomp = os.path.join(
            test_settings.TEST_DATA_DIR, 'resizer',
            'test-reference-resizecomp.jpeg'
        )

    def _load_image_as_str(self, file):
        return open(file).read()

    def test_resize_crop(self):
        image = self._load_image_as_str(self.test_in)
        reference = self._load_image_as_str(self.test_reference_crop)
        reference_hash = hashlib.md5(reference).hexdigest()

        res = Resizer(engine.BobRossEngine())
        out = res._resize_using_pg(image, 200, 200, 'crop')
        out_file = out[0]
        out_file_hash = hashlib.md5(out_file).hexdigest()

        self.assertEqual(out_file_hash, reference_hash)
        self.assertEqual(out[1], 200)
        self.assertEqual(out[2], 200)

    def test_resize_resize(self):
        image = self._load_image_as_str(self.test_in)
        reference = self._load_image_as_str(self.test_reference_resize)
        reference_hash = hashlib.md5(reference).hexdigest()

        res = Resizer(engine.BobRossEngine())
        out = res._resize_using_pg(image, 200, 200, 'resize')
        out_file = out[0]
        out_file_hash = hashlib.md5(out_file).hexdigest()

        self.assertEqual(out_file_hash, reference_hash)
        self.assertEqual(out[1], 200)
        self.assertEqual(out[2], 151)

    def test_resize_resizecomp(self):
        image = self._load_image_as_str(self.test_in)
        reference = self._load_image_as_str(self.test_reference_resizecomp)
        reference_hash = hashlib.md5(reference).hexdigest()

        res = Resizer(engine.BobRossEngine())
        out = res._resize_using_pg(image, 200, 200, 'resizecomp')
        out_file = out[0]
        out_file_hash = hashlib.md5(out_file).hexdigest()

        self.assertEqual(out_file_hash, reference_hash)
        self.assertEqual(out[1], 200)
        self.assertEqual(out[2], 200)
