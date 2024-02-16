#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
@app.route('/')
def hello_HBNB():
	return 'Hello HBNB!'


if __name__ == '__main__':
	"""host and port"""
	app.run(host='0.0.0.0', port=5000)
