from __future__ import absolute_import, print_function, unicode_literals


class NoDataInS3Error(Exception):
    """ When S3 has no data in the key """
    pass
