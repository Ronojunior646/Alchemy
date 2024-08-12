from main import db

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    description= db.Column(db.String,nullable=False)
    cost = db.column(db.Integer,nullable=False)
    startdate = db.Column(db.Date,nullable=False)
    enddate = db.Column(db.Date,nullable=False)
    status = db.Column(db.Boolean,default=False)