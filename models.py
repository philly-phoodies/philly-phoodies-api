from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
	__tablename__ = 'Users'
	userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.Integer, nullable=False)
	password = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False)
	location = db.Column(db.String(128), nullable=False)

	def __init__(self, userid, username, password, email, location):
		self.userid = userid
		self.username = username
		self.password = password
		self.email = email
		self.location = location

class TypeFood(db.Model):
	__tablename__ = "Typefood"
	foodtypeid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128))

	def __init__(self, foodtypeid, name):
		self.foodtypeid = foodtypeid
		self.name = name

class Restaurant(db.Model):
	__tablename__ = "Restaurant"
	restaurantidid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128), nullable=False)
	address = db.Column(db.String(128))
	state = db.Column(db.String(128))
	pricepoint = db.Column(db.Integer)
	foodtypeid = db.Column(db.Integer, db.ForeignKey('Typefood.foodtypeid'), nullable=False)

	def __init__(self, restaurantidid, name, address, state, pricepoint, foodtypeid):
		self.restaurantidid = restaurantidid
		self.name = name
		self.address = address
		self.state = state
		self.pricepoint = pricepoint
		self.foodtypeid = foodtypeid


class Food(db.Model):
	__tablename__ = "Food"
	foodid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	restaurantidid = db.Column(db.Integer, db.ForeignKey('Restaurant.restaurantidid'), nullable=False, primary_key=True)

	def __init__(self, foodid, name, restaurantidid):
		self.foodid = foodid
		self.name = name
		self.restaurantidid = restaurantidid

