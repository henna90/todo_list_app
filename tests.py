""" Tests for TodoList Flask app"""
import unittest

from run import app, connect_to_db, db



class FlaskTests(unittest.TestCase):
    """Test for todo list site"""
    def setUp(self):
        """Completed before each test"""

        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_index(self):
        """Test the homepage is rendering correctly"""

        result = self.client.get('/')

        self.assertEqual(result.status_code, 200)
        self.assertNotIn(b'Login', result.data)


    # def test_login(self):
    #     """Tests the add user form is rendered"""

    #     result = self.client.get('/login')

    #     self.assertEqual(result.status_code, 200)
        # self.assertIn(b'username', result.data)

