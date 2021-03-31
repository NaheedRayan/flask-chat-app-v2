from flask import Blueprint,render_template
from flask_login import login_user , login_required , current_user
from .models import Room , Participant , Message , User



opt = Blueprint('opt' , __name__)


@opt.route('/options')
@login_required
def options_name():
    return render_template('options.html' , user = current_user)
