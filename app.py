#!/usr/bin/env python
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
	return "Hello There!"


if __name__ == '__main__':
	app.run()

