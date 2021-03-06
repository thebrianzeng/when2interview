from app.models.interviewee import Interviewee


def create_interviewee(name, availabilities, rc_id, email):
    new_interviewee = Interviewee(name=name, availabilities=availabilities, 
                                  rc_id=rc_id, email=email)
    new_interviewee.save()


def get_interviewees(rc_id):
    return Interviewee.objects(rc_id=rc_id)
