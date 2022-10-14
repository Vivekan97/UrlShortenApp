from datetime import datetime
from flask import Blueprint, redirect, url_for, request, jsonify, render_template
from .extensions import SECRET_KEY, db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

auth = Blueprint("auth", __name__, )


# endpoint for login returns auth token if success
@auth.route("/api/auth/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return jsonify(timestamp=datetime.now(), message="Invalid Request"), 400
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(timestamp=datetime.now(), message="User Not Registered"), 404
    if not check_password_hash(user.password, password):
        return jsonify(timestamp=datetime.now(), message="Incorrect Password"), 401
    
    token = user.encode_auth_token(user.id)
    return jsonify(timestamp=datetime.now(), message="Authentication Success", access_token=token), 200


# for registering new user
@auth.route("/api/auth/register", methods=["POST"])
def register():
    
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return jsonify(timestamp=datetime.now(), message="Invalid Request"), 400

    user = User.query.filter_by(email=email).first()
    
    if user:
        return jsonify(timestamp=datetime.now(), message="User Registered Already. Please Sign In"), 409
    new_user = User(email=email, password=generate_password_hash(password, method="sha256"))
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify(timestamp=datetime.now(), message="User Created"), 201


# for decoding the jwt token
@auth.route("/decode", methods=["POST"])
def decode():
    token = request.form.get("token")
    
    if not token:
        return "Invalid", 404
    
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return jsonify(result=decoded)


# for view function rendering the html
@auth.route("/signin", methods=["GET"])
def get_login():
    return render_template("index.html")


# for view function rendering the html
@auth.route("/register", methods=["GET"])
def get_register():
    return render_template("index.html")


# for view function rendering the html
@auth.route("/", methods=["GET"])
def get_home():
    return redirect(url_for("auth.get_login"))
