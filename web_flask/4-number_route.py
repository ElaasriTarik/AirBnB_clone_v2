#!/usr/bin/python3
"""tarek"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """hello hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """hello hbnb"""
    val = 'C '
    for c in text:
        if c != '_':
            val += c
        else:
            val += ' '
    return val


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py_text(text='is_cool'):
    """hello hbnb"""
    val = 'Python '
    for c in text:
        if c != '_':
            val += c
        else:
            val += ' '
    return val


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """hello hbnb"""
    if type(n) == int:
        n = escape(n)
        return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
