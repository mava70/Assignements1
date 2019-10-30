from webgetregion import app
import unittest

# python -m unittest webgetregion.py


class Testapp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        #assert b'Main' in rv.data
        #assert False

    def test_add(self):
        rv = self.app.get('/risorse')
        self.assertEqual(rv.status, '200 OK')
        #self.assertEqual(rv.data, '5')

        #rv = self.app.get('/info')
        #self.assertEqual(rv.status, '200 OK')
        #self.assertEqual(rv.data, '10')

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')
