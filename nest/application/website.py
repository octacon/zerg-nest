from twisted.application.internet import TCPServer
from twisted.web.server import Site
from twisted.web.resource import Resource


# TODO
class NestServerFactory(object):
    __DEFAULT_HOST = '0.0.0.0'
    __DEFAULT_PORT = 7200
    __DEFAULT_WEBSERVICES = {}

    def __init__(self, app):
        self.app = app
        self.host = NestServerFactory.__DEFAULT_HOST
        self.port = NestServerFactory.__DEFAULT_PORT
        self.webservices = NestServerFactory.__DEFAULT_WEBSERVICES

    def setHost(self, host):
        self.host = host
        return self

    def setPost(self, port):
        self.port = port
        return self

    def addService(self, path, service):
        self.webservices[path] = service
        return self

    def registry(self):
        root = NestRoot(self.app, debug=False)
        for (path, service) in self.webservices.items():
            root.putChild(path.encode('utf-8'), service(root))

        server = TCPServer(self.port, Site(root), interface=self.host)
        server.setServiceParent(self.app)
        return self.app


# TODO 注释
class NestRoot(Resource):

    def __init__(self, app, nodename='NEST', debug=True):
        Resource.__init__(self)
        self.debug = debug
        self.app = app
        self.nodename = nodename
