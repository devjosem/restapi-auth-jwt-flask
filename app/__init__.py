from flask import Flask

from .extensions.db import db
from .extensions.jwt import jwt
from dotenv import load_dotenv
import os
import sys
from datetime import timedelta

load_dotenv()


def require_env(name: str) -> str:
    val = os.getenv(name)
    if not val:
        sys.exit(f"FATAL: Variável obrigatória {name} não definida ou vazia")
    return val


def create_app():

    app = Flask(__name__)
    
    app.secret_key = require_env("APP_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = require_env("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.config["JWT_SECRET_KEY"] = require_env("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes= 15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days= 30)

    from .models.user import User


    db.init_app(app)
    jwt.init_app(app)

    return app
