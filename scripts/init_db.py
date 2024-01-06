# scripts/init_db.py
import logging
from src.app.app import db


def initialize_database(app):
    logging.info("Starting database initialization.")
    with app.app_context():
        try:
            db.create_all()
            logging.info("Database tables created successfully.")
        except Exception as e:
            logging.error("Error occurred during database initialization: %s", e)
