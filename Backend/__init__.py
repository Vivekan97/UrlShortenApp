from flask import Flask
from flask_cors import CORS
from .extensions import db, SECRET_KEY


def create_app():
    
    app = Flask(__name__, static_url_path="", static_folder="static")
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    CORS(app)
    
    from .models import User
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
