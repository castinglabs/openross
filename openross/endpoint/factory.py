from __future__ import absolute_import, print_function, unicode_literals

from twisted.web import server

from openross.endpoint import BobRossEndpoint


def get_factory():
    """ Build site from twisted endpoint """

    root = BobRossEndpoint()
    return server.Site(root)
