from __future__ import absolute_import


class NoDataInS3Error(Exception):
    """ When S3 has no data in the key """
    pass
