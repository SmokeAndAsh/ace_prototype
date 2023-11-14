# src/networking/gateway/clients/web_cli.py

from flask import Flask

web_app = Flask(__name__)


@web_app.route('/')
def home():
    return "Networking Module Dashboard"


