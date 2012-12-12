from werkzeug.contrib.cache import MemcachedCache
from flask.sessions import SessionInterface, SessionMixin
import os

class Memsession(object):

    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        app.session_interface = MemcachedSessionInterface()

class MemcachedSession(dict, SessionMixin): pass

class MemcachedSessionInterface(SessionInterface):
    
    session_class = MemcachedSession

    def get_connection(self, app):
        servers = app.config.get('MEMCACHED_SERVERS')
        username = app.config.get('MEMCACHED_USERNAME')
        password = app.config.get('MEMCACHED_PASSWORD')
        cache = MemcachedCache(servers, username, password)
        
        if not cache:
            raise Exception('Memcached session cannot connect to memcached server.')
        return cache

    def open_session(self, app, request):
        self.cookie_session_id = request.cookies.get(app.session_cookie_name, None)
        self.session_new = False
        
        if not self.cookie_session_id:
            self.cookie_session_id = os.urandom(40).encode('hex')
            self.session_new = True

        if not request.remote_addr:
            self.memsess_id = '@'.join(['nobody', self.cookie_session_id])
        else:
            self.memsess_id = '@'.join([request.remote_addr, self.cookie_session_id])

        cache = self.get_connection(app)
        session = cache.get(self.memsess_id) or {}
        cache.set(self.memsess_id, session)
        return self.session_class(session)

    def save_session(self, app, session, response):
        expires = self.get_expiration_time(app, session)
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        cache = self.get_connection(app)
        cache.set(self.memsess_id, session)
        if self.session_new:
            response.set_cookie(app.session_cookie_name, self.cookie_session_id, path=path,
                                expires=expires, httponly=httponly,
                                secure=secure, domain=domain)