from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# for admin page
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# creating the object for database
db = SQLAlchemy()
DB_NAME = "database.db"


# for creating the app
def create_app():
    # initializing the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Any secret key"
    
    # initializing the data base
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # for debugging sql
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)

    # now for registering the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefix='/')
    app.register_blueprint(auth , url_prefix='/')

    # for creating database
    from .models import User , Room , Participant , Message
    # from .models import User,Note
    create_database(app)


    # for mannaging the user login
    # if the user is not logged in then he/she will be redirected to auth.login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader 
    def load_user(id):
        return User.query.get(int(id))


    # for admin page
    admin = Admin(app)
    class ChildView(ModelView):
        column_display_pk = True # optional, but I like to see the IDs in the list
        column_hide_backrefs = False
    
    admin.add_view(ChildView(User, db.session))
    admin.add_view(ChildView(Room, db.session))
    admin.add_view(ChildView(Participant, db.session))
    admin.add_view(ChildView(Message, db.session))
    
    return app


def create_database(app):
    # if the database does not exist then we will create it
    if not path.exists('website/'+DB_NAME):
        db.create_all(app = app)
        print('Database created')