from app import db

class Interviewee(db.Document):
    name = db.StringField(max_length=70)
    slots = db.ListField()
