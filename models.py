from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Users(db.Model):
	__tablename__ = 'Users'
	username = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False)
	location = db.Column(db.String(128), nullable=False)


class TypeFood(db.Model):
	__tablename__ = "Typefood"
	foodtypeid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128)


