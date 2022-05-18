
from os import link
from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(600),index=True)
    prof_pic = db.Column(db.String())
    password_hash = (db.String(30))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

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
    
class Tracks:
    def __init__(self,id,title,link,preview,artistId,artistName,albumId,albumImage):
        self.id = id
        self.title = title
        self.link = link
        self.preview = preview
        self.artistId = artistId
        self.artistName = artistName
        self.albumId = albumId
        self.albumImage = albumImage

class Albums:
    def __init__(self,id, title,link,artistId,artistName,albumImage):
        self.id = id
        self.title = title
        self.link = link
        self.artistId = artistId
        self.artistName = artistName
        self.albumImage = albumImage

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    album_id = db.Column(db.Integer)
    album_title = db.Column(db.String)
    image_path = db.Column(db.String)
    album_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(album_id=id).all()
        return reviews

