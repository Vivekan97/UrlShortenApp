from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

SECRET_KEY = "WINGARDIUM_LEVIOSA"   # for jwt token

db = SQLAlchemy()   # db instance

jwt = JWTManager()  # jwt manager instance to handle jwt functionalities
