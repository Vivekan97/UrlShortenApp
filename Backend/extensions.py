from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

SECRET_KEY = "VIRTUAL-CLIENT-KEY"

db = SQLAlchemy()

jwt = JWTManager()