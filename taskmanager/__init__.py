import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRECT_KEY"] = os.environ.get("SECRECT_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

DB = SQLAlchemy(app)

from taskmanager import routes
