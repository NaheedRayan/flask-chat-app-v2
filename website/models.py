from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



# The User will inherit database model and UserMixin . The UserMixin is for authentication
# purpose
class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150) , unique = True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    

    rooms = db.relationship("Room" , backref = "user")
    participants = db.relationship("Participant" , backref = "user")
    messages = db.relationship("Message" , backref = "user")
    #sudo coloumns in Room , Participant , Message
    # rooms_userid = db.relationship('Room',backref=db.backref('user-id'))
    # participants_userid = db.relationship('Participant',backref=db.backref('user-id'))
    # message_userid = db.relationship('Message' , backref = db.backref('user-id'))


    # def __repr__(self):
    #     return f"User('{self.username}','{self.userEmail}','{self.image_file}')"

    

    


class Room(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    roomid = db.Column(db.String(150) , unique = True)
    
    userid = db.Column(db.String(150),db.ForeignKey('user.id'))

    participants = db.relationship("Participant" , backref = "room")
    messages = db.relationship("Message" , backref = "room")

    #sudo coloumns in Participant , Message
    # participants_roomid = db.relationship('Participant',backref=db.backref('room-id'))
    # message_roomid = db.relationship('Message' , backref = db.backref('user-id'))



class Participant(db.Model):
    id = db.Column(db.Integer , primary_key = True)

    userid = db.Column(db.String(150),db.ForeignKey('user.id'))
    roomid = db.Column(db.String(150),db.ForeignKey('room.roomid'))

class Message(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    message = db.Column(db.String(10000))

    userid = db.Column(db.String(150),db.ForeignKey('user.id'))
    roomid = db.Column(db.String(150),db.ForeignKey('room.roomid'))
    


