from mediadrop.lib.base import BaseController
from mediadrop.lib.decorators import expose
from dragontv_plugin.forms.offcampusform import OffcampusForm

offcampus_form = OffcampusForm()

class OffcampusController(BaseController):

    @expose('offcampus/index.html')
    def index(self, **kwargs):
		return dict(
			title="That location is unavailable",
			message = "You must be at SSIS and have your VPN turned off for full access to DragonTV.",
			redirect = "You will now automatically be redirected to a publically available area.",
			)

__controller__ = OffcampusController