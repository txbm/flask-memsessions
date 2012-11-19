from werkzeug.contrib.cache import MemcachedCache
from flask.session import SessionMixin

class Memsession(object):

	def __init__(self, app=None):
		if app is not None:
			self.app = app
			self.init_app(self.app)
		else:
			self.app = None

	def init_app(self, app):
		app.config.setdefault('MEMSESS_HOST', '127.0.0.1:11211')
		if hasattr(app, 'teardown_context'):
			app.teardown_appcontext(self.teardown)
		else:
			app.teardown_request(self.teardown)

class MemcachedSession(dict, SessionMixin):
	pass
