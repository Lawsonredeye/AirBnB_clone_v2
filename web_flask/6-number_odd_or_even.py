#!/usr/bin/python3
"""
this just starts a flask web application
and returns HBNB with Hello HBNB!
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """Just returns Hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Just print anything along sides c"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Prints what ever text would be"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """displays only numbers"""
    if n >= 0:
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number(n):
    """returns an html page"""
    if n >= 0:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Prints even or odd after calculations"""
    if n % 2 == 0:
        n = f"{n} is even"
    else:
        n = f"{n} is odd"
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
