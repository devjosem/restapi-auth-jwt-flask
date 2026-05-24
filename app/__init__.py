from flask import Flask

from extensions import db, jwt
from dotenv import load_dotenv
import os
import sys
from datetime import timedelta

def check_env():
    app_secret_key = os.getenv("APP_SECRET_KEY")
    database_uri = os.getenv("DATABASE_URI")
    jwt_secret_key = os.getenv("JWT_SECRET_KEY")

    if not app_secret_key or not database_uri or not jwt_secret_key:
        return sys.exit("CONFIGURACOES INCOMPLETAS,,,,")


def create_app():

    app = Flask(__name__)

    load_dotenv()

    check_env()
    
    app.secret_key = os.getenv("APP_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes= 15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes= 15)


    db.init_app(app)
    jwt.init_app(app)

    return app
