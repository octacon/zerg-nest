from scrapyd import get_application
from nest.application.website import NestServerFactory

from nest.restful.daemonstatus import Instance

scrapydApp = get_application()

application = NestServerFactory(scrapydApp) \
    .addService('hello', Instance) \
    .registry()
