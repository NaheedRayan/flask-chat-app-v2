from flask import Blueprint,render_template ,request ,redirect ,url_for , flash
from flask_login import login_user , login_required , current_user
from .models import Room , Participant , Message , User
from website import db



opt = Blueprint('opt' , __name__)


@opt.route('/options' , methods=['GET' , 'POST'])
@login_required
def options_name():
    if request.method == 'POST':
        groupname = request.form.get('groupname')
        groupsize = request.form.get('groupsize')
        joingroup = request.form.get('joingroup')
        leavegroup = request.form.get('leavegroup')


        # print('-------------------------------------------------------------------')
        # print(groupname , groupsize ,joingroup , leavegroup)

        if (groupname != None and groupsize != None):
            
            room = Room.query.filter_by(roomid= groupname).first()
            # if the room doesnt exist then we will create a room
            if room :
                flash('The Group name exists! Please enter another group name' ,category= 'error')
            
            elif (len(groupname)<3):
                flash('Group name must be greater than 3' ,category= 'error')

            elif int(groupsize) < 2:
                flash('Group size must be greater than 1' ,category= 'error')

            else:
                # added a room
                new_room = Room(roomid = groupname , userid = current_user.id , grouplimit = groupsize)
                db.session.add(new_room)
                db.session.commit()

                roomid = Room.query.filter_by(roomid= groupname).first()
                new_participant = Participant(userid = current_user.id , roomid = roomid.id , roomname = groupname)
                db.session.add(new_participant)
                db.session.commit()
                # adding participant info

                flash('Group created' ,category= 'success')
                return redirect(url_for('views.chat'))

        elif joingroup != None:
            room = Room.query.filter_by(roomid= joingroup).first()

            # if the room exists then we will see if it belongs to the user or not
            if(len(joingroup) < 1):
                flash('Invalid Input' ,category= 'error')

            
            elif room :
                if room.userid != current_user.id:
                    new_participant = Participant(userid = current_user.id , roomid = room.id , roomname = joingroup)
                    db.session.add(new_participant)
                    db.session.commit()
                    
                    flash('Joined Group' ,category= 'success')
                    return redirect(url_for('views.chat'))

            
            else:
                flash('The group doesnot exist' ,category= 'error')

                



        elif leavegroup!= None:
            flash('The feature will be available soon' ,category= 'success')
            return redirect(url_for('views.chat'))

        else :
            print('not ok')


    return render_template('options.html' , user = current_user)
