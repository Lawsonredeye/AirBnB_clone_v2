#!/usr/bin/python3
"""
this just starts a flask web application
and returns HBNB with Hello HBNB!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """Just returns Hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
