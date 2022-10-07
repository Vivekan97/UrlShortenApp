from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from shortener import get_shortened_url, get_long_url

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def homepage():
    return jsonify(message="Welcome to URL Shortener")


@app.route("/short", methods=["POST"])
def short_url():
    source = request.get_json()
    if "url" not in source.keys():
        return jsonify(input=None, result=None, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    source_url = source["url"]
    short = get_shortened_url(source_url)
    if short is None:
        return jsonify(input=source_url, result=short, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    return jsonify(input=source_url, result=short, timestamp=datetime.now())


@app.route("/long", methods=["POST"])
def long_url():
    source = request.get_json()
    if "url" not in source.keys():
        return jsonify(input=None, result=None, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    source_url = source["url"]
    long = get_long_url(source_url)
    if long is None:
        return jsonify(input=source_url, result=long, message="Invalid URL. Cannot process !",
                       timestamp=datetime.now()), 400
    return jsonify(input=source_url, result=long, timestamp=datetime.now())


if __name__ == "__main__":
    app.run(debug=True)
