#!/usr/bin/env python
from flask import Flask, jsonify
import requests
import json
from config import *
from models import *
from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

@app.route("/", methods = ["GET"])
def home():
	users = db.session.query(Users)
	results = Users.query.all()
	return json.dumps(results, cls=AlchemyEncoder)


@app.route("/searchme/<searchitem>", methods=["GET"])
def searchme(searchitem):
	pass

@app.route("/searchrestaurant/<restaurant>", methods = ["GET"])
def searchrestaurant(restaurant):
	results = db.session.query(Restaurant).filter(Restaurant.restaurantname==restaurant).first()
	return json.dumps(results, cls=AlchemyEncoder)


if __name__ == '__main__':
	app.run()

