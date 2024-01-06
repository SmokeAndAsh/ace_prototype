# src/app/app.py
import os
import secrets
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from prometheus_flask_exporter import PrometheusMetrics
from config.config import DevelopmentConfig, ProductionConfig, TestingConfig

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.abspath(os.path.join(base_dir, "../../templates"))

    # Create a Flask instance
    app = Flask(__name__, template_folder=template_dir)
    metrics = PrometheusMetrics(app)
    app.secret_key = os.getenv("FLASK_SECRET")
    app.config.from_object(config_class)

    # Determine the configuration to load based on the FLASK_ENV environment variable
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Initialize plugins
    db.init_app(app)

    # OAuth setup
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    oauth = OAuth(app)
    keycloak = oauth.register(
        name='keycloak',
        client_id=client_id,
        client_secret=client_secret,
        server_metadata_url='http://localhost:8080/realms/ace-lite/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid profile email'},
    )

    # Setup logging
    setup_logging(app)

    # Define your Flask routes here
    @app.route('/')
    def main():
        app.logger.info('Serving the main route')
        user_info = session.get('user_info', None)
        if user_info:
            return render_template('home.html', user_info=user_info)
        else:
            return redirect(url_for('login'))

    @app.route('/login')
    def login():
        nonce = secrets.token_urlsafe(16)
        session['nonce'] = nonce
        app.logger.info('Serving the login route')
        redirect_uri = url_for('auth', _external=True)
        return render_template('login.html')

    @app.route('/auth')
    def auth():
        app.logger.info('Authorizing...')
        try:
            token = keycloak.authorize_access_token()
            nonce = session.pop('nonce', None)

            user_info = keycloak.parse_id_token(token, nonce=nonce)
            create_session(user_info, token)
            app.logger.info('Authorization successful')

            return redirect('/')
        except Exception as e:
            return f"Authorization Error: {e}"

    @app.route('/logout')
    def logout():
        app.logger.info('Logging out')
        session.clear()
        return redirect('/')

    metrics.info('app_info', 'Application info', version='1.0.1')

    return app


def setup_logging(app):
    if app.config["DEBUG"]:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    if not app.debug:
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = RotatingFileHandler(os.path.join(log_dir, 'app.log'), maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)


def create_session(user_info, token):
    session['user_info'] = user_info
    session['token'] = token


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=app.config['DEBUG'])
