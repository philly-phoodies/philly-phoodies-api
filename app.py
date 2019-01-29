#!/usr/bin/env python
from flask import Flask, jsonify
import requests
from config import *
from models import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)



@app.route("/", methods = ["GET"])
def home():
	return "Hello There!"


if __name__ == '__main__':
	app.run()

