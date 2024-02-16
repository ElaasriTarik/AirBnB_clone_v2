#!/usr/bin/python3
"""tarek"""
from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_HBNB():
    """hello hbnb"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """host and port"""
    app.run(host='0.0.0.0', port=5000)
