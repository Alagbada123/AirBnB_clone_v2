#!/usr/bin/python3
""" Web application listening on the 0.0.0.0, port 5000 """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displays Hello HBNB! on home route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Displays HBNB! on hbnb route """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Displays 'C' followed by the value of text
    Replaces underscores with a space
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
