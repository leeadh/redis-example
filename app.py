#!/usr/bin/python

from flask import Flask, render_template
from redis import Redis
import os

app = Flask(__name__)
#192.168.1.107
host = os.environ['REDIS_SERVICE']
redis = Redis(host=host, port=6379)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """ Return the homepage counter """
    counter = redis.incr("hits")
    print("CHECKING PORT")
    print(counter)
    return render_template("index.html",counter=counter)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )