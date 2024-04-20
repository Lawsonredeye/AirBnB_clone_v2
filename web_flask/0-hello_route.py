#!/usr/bin/python3
"""
First time learning flask web framework
this is just for learning how to use flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    default landing page that has the content hello
    """
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


