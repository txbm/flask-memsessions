import unittest
import flask
from werkzeug.contrib.cache import MemcachedCache
from flask_memsessions import Memsession, MemcachedSessionInterface, MemcachedSession


class MemsessionTest(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask(__name__)
        self.mem = Memsession()
        self.mem.init_app(self.app)

    def test_simple(self):
        self.assertIsInstance(self.app.session_interface, MemcachedSessionInterface)

    def test_connection(self):
        c = MemcachedSessionInterface()
        cn = c.get_connection(self.app)

        self.assertIsInstance(cn, MemcachedCache)

    def test_session(self):
        with self.app.test_client() as c:
            with c.session_transaction() as s:
                s['test_key'] = 'test value'

            self.assertEqual(s['test_key'], 'test value')


if __name__ =='__main__':
    unittest.main()