from website import create_app
from flask_socketio import SocketIO , join_room , leave_room
from website.models import Room , Participant , Message , User
from flask_login import current_user
from website import db

app = create_app()
socketio = SocketIO(app)


@socketio.on('join_room')
def handle_join_room_event(data):
   
    # here app.logger is used instead of print because it also prints the time of log.
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    # then it will create a room using the join_room function .
    # Then it will call a join_room_announcement event in chat.html and send data
    # and emit the join room announcement in the created room.
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])

@socketio.on('send_message')
def handle_send_message_event(data):
    
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))


    # emmiting the message
    socketio.emit('receive_message', data, room=data['room'])


    # here we will save the message in database and emit it in the database
    new_message = Message(message = data['message'] , username = data['username'], userid = current_user.id , roomid = data['room'])            
    db.session.add(new_message)
    db.session.commit()

# if someone left the room then we will announce it
@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    # if the room is empty we will not emit any message
    if len(data['room']) > 0 :
        leave_room(data['room'])
        socketio.emit('leave_room_announcement', data, room=data['room'])

 
    
    



if __name__ == '__main__':
    # This is a debugging server
    app.run(host = '0.0.0.0' , port = 5000 ,debug = True)