from flask import Flask
from config import Config
import os
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

SQLACHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLACHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app/db"
# app.config.from_object(Config)



from app import routes, models





