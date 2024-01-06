# config/config.py
import os


class Config:
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# noinspection PyCompatibility
class DevelopmentConfig(Config):
    """Development configuration."""
    host = os.getenv("DB_HOST", "postgres")
    port = os.getenv("DB_PORT", "5432")
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{host}:{port}/{os.getenv("DB_NAME")}'
    DEBUG = True


# noinspection PyCompatibility
class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.getenv("PROD_DB_USERNAME")}:{os.getenv("PROD_DB_PASSWORD")}@postgres/{os.getenv("PROD_DB_NAME")}'
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = True
