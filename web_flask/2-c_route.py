#!/usr/bin/python3
"""Displays hello world."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """
        Does nothing but says hello.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def say_HBHB():
    """
        Does nothing but says HBNB.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_text(text):
    return 'C {}'.format(' '.join(text.split('_')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
