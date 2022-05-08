from . import db 
from flask_login import UserMixin, current_user 
from datetime import datetime 
from werkzeug.security import generate_password_hash,check_password_hash 
from . import login_manager  


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter 
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_user(self): 
        db.session.add(self)
        db.session.commit()

    # def delete_user(self):
    #     db.session.delete(self)
    #     db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False) 


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments

    def __repr__(self):
        return f'comment:{self.comment}'



class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    category = db.Column(db.String(255),nullable = False)
    text = db.Column(db.String, nullable = False)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    posted = db.Column(db.DateTime,default=datetime.utcnow) 
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_category(cls, category):
        category = Pitch.query.filter_by(category=category).all()
        return category 
    
    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Pitch: {self.text}'



class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()
        return upvotes 
        
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}' 
    
    

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_downvotes(cls,id):
        downvotes = Downvote.query.filter_by(pitch_id=id).all()
        return downvotes 

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'