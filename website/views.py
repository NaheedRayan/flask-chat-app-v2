from flask import Blueprint,render_template
from flask_login import login_user , login_required , current_user
from .models import Room , Participant , Message , User


views = Blueprint('views' , __name__)


@views.route('/')
def home():
    return render_template('home.html', user = current_user)


@views.route('/chat')
@views.route('/chat/<room_id>')
@login_required
def chat(room_id = ''):

    # by default the chat area will show nothing . But when a group is pressed
    # we will get its room id
    # with the help of room_id we will filter the messages.
    rooms = Participant.query.filter_by(userid = current_user.id).all()    
    # now getting the messages of the room_id
    messages = Message.query.order_by(Message.date).filter_by(roomid = room_id).all()

    # for roomname
    room_name = Room.query.filter_by(id = room_id).first()


    return render_template('chat.html', user = current_user , rooms = rooms , messages = messages , room_id = room_id , room_name = room_name)