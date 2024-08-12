from main import db

class Booking:
    __tablenamme__="bookings"
    id = db.column(db.Integer, primary_key=True, nullable=False)
    student_id = db.column(db.Integer, db.integer, nullable=False)
    course_id = db.column(db.Integer, db.integer, nullable=False)
    completion_status = db.column(db.Boolean, default=False)
    created_date = db.column(db.DateTime, nullable=False)
    Booking_payment = db.relationship('Payment', backref='booking')