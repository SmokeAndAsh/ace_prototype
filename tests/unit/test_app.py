# tests/unit/test_app.py
import unittest
from src.app.app import app, db, User


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Configure the app for testing
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        # Send a request to the application.
        response = self.app.get('/')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected content.
        self.assertIn(b'Hello, World!', response.data)


if __name__ == '__main__':
    unittest.main()

