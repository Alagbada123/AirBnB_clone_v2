#!/usr/bin/python3
"""Displays hello world."""
from flask import Flask, render_template

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
def c_text(text):
    return 'C {}'.format(' '.join(text.split('_')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool_or_text(text='is cool'):
    return 'Python {}'.format(' '.join(text.split('_')))

@app.route('/number/<int:n>', strict_slashes=False)
def n_is_a_number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def n_is_a_number_template(n):
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
