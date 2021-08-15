from flask import Flask
from flask_cors import CORS

# Import the calculation's blueprint
from calculation.routes import calculation

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register the blueprint
    app.register_blueprint(calculation)

    return app