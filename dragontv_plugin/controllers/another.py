from mediadrop.lib.base import BaseController
from mediadrop.lib.decorators import expose

class AnotherController(BaseController):

    @expose('index.html')	
    def index(self, **kwargs):
		from IPython import embed
		embed()
		return {}

__controller__ = AnotherController