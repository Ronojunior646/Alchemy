from main import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    national_id = db.Column(db.integer)
    status = db.Column(db.boolean)
    bookings = db.relationship('Booking', backref='student')