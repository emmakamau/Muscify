from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(600),index=True)
    prof_pic = db.Column(db.String())
    blogs = db.relationship('Blog',backref='user',lazy ='dynamic')
    comments = db.relationship('Comment',backref='user',lazy ='dynamic')
    password_hash = (db.String(30))

    pass_secure=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('Password attribute is not readable')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __refr__(self):
        return f'User{self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Chart:
    def __init__(self,id,title,link,preview):
        self.id = id
        self.title = title
        self.link = link
        self.preview = preview
