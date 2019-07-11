from scrapyd.webservice import WsResource
from scrapyd.webservice import DaemonStatus


class Instance(WsResource):

    def __init__(self, root):
        super().__init__(root)

    def render_GET(self, request):
        return {'hello': 'world'}

    def render_POST(self):
        # print(request)
        return {'error': 'notSupport'}
