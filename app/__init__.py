from atexit import register
from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #Creating app cofiguration
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)

    #Registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    return app