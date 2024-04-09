#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    try:
        return '{} is an integer'.format(n)
    except TypeError:
        return '{} must be an integer'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
