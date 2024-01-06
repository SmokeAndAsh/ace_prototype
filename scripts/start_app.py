# scripts/start_app.py
import os
from src.app.app import create_app

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    app.run(debug=True)
