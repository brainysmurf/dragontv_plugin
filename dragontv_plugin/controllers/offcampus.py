from mediadrop.lib.base import BaseController
from mediadrop.lib.decorators import expose
from dragontv_plugin.forms.offcampusform import OffcampusForm

offcampus_form = OffcampusForm()

class OffcampusController(BaseController):

    @expose('offcampus/index.html')
    def index(self, **kwargs):
		return dict(
			title="That location is unavailable",
			message = "The area you tried to navigate to is unavailable. You must be at SSIS and have your VPN turned off.",
			redirect = "You will now be redirected to an available area.",
			)

__controller__ = OffcampusController