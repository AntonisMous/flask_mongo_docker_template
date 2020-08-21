from flask import Flask
from flask_bcrypt import Bcrypt

from .config import config_by_name
from .util.mongodb_handler import MongodbHandler
from .log.logger import Logger
from .controller.routes import init_routes


mongo = MongodbHandler()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__, template_folder='./main/templates')
    app.config.from_object(config_by_name[config_name])
    Logger.init_app(app)
    mongo.init_app(app)
    flask_bcrypt.init_app(app)
    init_routes(app)

    return app
