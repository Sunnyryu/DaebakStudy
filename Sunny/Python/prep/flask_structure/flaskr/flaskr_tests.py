import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.DATABASE)

    def test_empty_db(self):
        rv = self.app.get('/')
        a = 'No entries here so far'
        k = a.encode('utf-8')
        assert k in rv.data
    # python3에서는 encode를 하여야 byte 에러가 나지 않는다.!
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        l_1 = 'You were logged in'.encode('utf-8')
        l_2 = 'You were logged out'.encode('utf-8')
        l_3 = 'Invalid username'.encode('utf-8')
        l_4 = 'Invalid password'.encode('utf-8')
        rv = self.login('admin', 'default')
        assert l_1 in rv.data
        rv = self.logout()
        assert l_2 in rv.data
        rv = self.login('adminx', 'default')
        assert l_3 in rv.data
        rv = self.login('admin', 'defaultx')
        assert l_4 in rv.data
        
    def test_messages(self):
        m_1 = 'No entries here so far'.encode('utf-8')
        m_2 = '&lt;Hello&gt;'.encode('utf-8')
        m_3 = '<strong>HTML</strong> allowed here'.encode('utf-8')
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert m_1 not in rv.data
        assert m_2 in rv.data
        assert m_3 in rv.data


if __name__ == '__main__':
    unittest.main()
