from app import db

class Interviewer(db.Document):
    name = db.StringField(max_length=70)
    availabilities = db.ListField()
    rc_id = db.StringField(max_length=50)
