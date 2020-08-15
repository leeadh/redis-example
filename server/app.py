#!/usr/bin/python

from flask import Flask, render_template, jsonify
from redis import Redis
import os
import json

app = Flask(__name__)
#192.168.1.107
host = os.environ['REDIS_SERVICE']
redis = Redis(host=host, port=6379)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET", "POST"])
def index():
    counter = redis.incr("hits")
    return render_template("index.html",counter=counter)

@app.route("/getdata", methods=["GET"])
def get_data():
    data = redis.get("hits")
    result = int(data)
    return jsonify({'count': result})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )