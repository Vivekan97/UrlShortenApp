from datetime import datetime
import json 
from flask import Blueprint, redirect, url_for, request,jsonify
from .extensions import SECRET_KEY, db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

import jwt

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(timestamp=datetime.now(),message="User Not Registered"), 404
    if  not check_password_hash(user.password, password):
        return jsonify(timestamp=datetime.now(),message="Incorrect Password"), 401
    
    token = user.encode_auth_token(user.id)
    print(token, user.decode_auth_token(token))
    # return token
    return jsonify(timestamp=datetime.now(),message="Authentication Success",access_token=token),200


@auth.route("/register", methods=["POST"])
def register():
    
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if user:
        return jsonify(timestamp=datetime.now(),message="User Registered Already. Please Sign In"), 409
    print(email,password)
    new_user = User(email=email, password=generate_password_hash(password, method="sha256"))
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify(timestamp=datetime.now(),message="User Created"), 201


@auth.route("/decode", methods=["POST"])
def decode():
    token = request.form.get("token")
    
    if not token:
        return "Invalid", 404
    
    decoded = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
    print(decoded)
    return jsonify(result=decoded)