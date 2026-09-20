from flask import Flask
from flask_cors import CORS

from config import DevelopmentConfig
from app.database import init_db
from app.routes import pages, api


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    CORS(app, origins=app.config["CORS_ORIGINS"])

    init_db(app)

    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/health")
    def health():
        return {
            "basari": True,
            "durum": "aktif"
        }

    return app