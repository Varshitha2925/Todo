from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ Allow frontend requests
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    mongo.init_app(app)

    from app.routes.task_routes import task_routes
    app.register_blueprint(task_routes)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        return response

    return app
