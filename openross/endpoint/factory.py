from __future__ import absolute_import

from twisted.web import server

from openross.endpoint import BobRossEndpoint


def get_factory():
    """ Build site from twisted endpoint """

    root = BobRossEndpoint()
    return server.Site(root)
