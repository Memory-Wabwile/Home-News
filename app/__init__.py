from flask import Flask
from flask import Blueprint
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    
    app = Flask(__name__) # Initializing application

    #Creating the app configuration
    app.config.from_object(config_options[config_name])

    #initializing the flask extension
    bootstrap.init_app(app)

   # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

   #setting config
    from .request import configure_request
    configure_request(app)

    return app
   