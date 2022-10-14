from flask import Flask
from flask_cors import CORS
from .extensions import db, SECRET_KEY, jwt


def create_app():
    
    app = Flask(__name__, static_url_path="", static_folder="static")
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    CORS(app)
    
    # for creating db instance it is must
    from .models import User
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # creating db if not exist
    with app.app_context():
        db.init_app(app)
        db.create_all()
    jwt.init_app(app)    
    return app
