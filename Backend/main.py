from datetime import datetime   # for getting the timestamp
from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS
# from shortener file importing
from .shortener import get_shortened_url, get_long_url
# from jwt import 
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from .token_manager import token_required

# added CORS and static folder path is mentioned explicitly
# app = Flask(__name__, static_url_path="", static_folder="static")
# CORS(app)
    
main = Blueprint("main", __name__)
# jwt = JWTManager(main)

# starting route to display the UI Page
@main.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


# for shortening the url by receiving the url in JSON request body
@main.route("/short", methods=["POST"])
# @jwt_required
@token_required
def short_url():
    source = request.get_json()
    # checking if url key present in the request body
    if "url" not in source.keys():
        return jsonify(input=None, result=None, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    source_url = source["url"]
    short = get_shortened_url(source_url)
    # incase if function throws error or returned None
    if short is None:
        return jsonify(input=source_url, result=short, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    # if no error and success
    return jsonify(input=source_url, result=short, timestamp=datetime.now())


# for retrieving the short url by receiving the url in JSON request body
@main.route("/long", methods=["POST"])
def long_url():
    source = request.get_json()
    # checking if url key present in the request body
    if "url" not in source.keys():
        return jsonify(input=None, result=None, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    source_url = source["url"]
    long = get_long_url(source_url)
    # incase if function throws error or returned None
    if long is None:
        return jsonify(input=source_url, result=long, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    # if no error and success
    return jsonify(input=source_url, result=long, timestamp=datetime.now())


# if __name__ == "__main__":
#     main.run()
