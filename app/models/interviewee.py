from app import db

class Interviewee(db.Document):
    name = db.StringField(max_length=70)
    availabilities = db.ListField()
    rc_id = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
