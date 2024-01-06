# tests/unit/test_db_init.py
import unittest
import logging
from src.app.app import create_app
from config.config import TestingConfig
from scripts.init_db import initialize_database

logging.basicConfig(level=logging.DEBUG)


class SimpleDatabaseTestCase(unittest.TestCase):
    def test_init_db(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        initialize_database(self.app)


if __name__ == '__main__':
    unittest.main()
