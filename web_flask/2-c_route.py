#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns hello hbnb"""
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_cool(text):
    """replaces underscores with space"""
    swap = text.replace("_", " ")
    return F"C {swap}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
