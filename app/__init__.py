from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing the flask extension
bootstrap = Bootstrap(app)

from app import views