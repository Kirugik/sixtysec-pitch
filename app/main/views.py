from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitch,Comment,Upvote,Downvote 
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required, current_user 
from .. import db,photos  


# views
@main.route('/')  
def index():
    pitches = Pitch.query.all()
    elevator = Pitch.query.filter_by(category='Elevator pitch').all()
    interview = Pitch.query.filter_by(category='Interview pitch').all() 
    pickup = Pitch.query.filter_by(category='Pickup line').all()
    pun = Pitch.query.filter_by(category='Pun').all() 
    return render_template('index.html', pitches=pitches, elevator=elevator, interview=interview, pickup=pickup, pun=pun)


@main.route('/pitch')
def pitch():
    pitches = Pitch.query.all()
    likes = Upvote.query.all()
    dislikes = Downvote.query.all()
    user_id = current_user
    return render_template('pitches.html', pitches=pitches, likes=likes, dislikes=dislikes, user_id=user_id)  


@main.route('/new_pitch', methods = ['POST','GET'])
@login_required 
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        category = form.category.data
        user_id = current_user

        # new pitch object
        new_pitch = Pitch(title=title, text=text, category=category, user_id=current_user._get_current_object().id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index')) 

    return render_template('new_pitch.html', form=form) 


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required 
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id

        # new comment object
        new_comment = Comment(comment=comment, pitch_id = pitch_id, user_id = user_id)

        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id=pitch_id))
    
    return render_template('comments.html', form=form, pitch=pitch, commnets=comments) 


@main.route('/user/<name>')
def user_profile(name): 
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    text = Pitch.query.filter_by(user_id = user_id).all()
    
    if user is None: 
        abort(404)
    return render_template('profile/user_profile.html', user=user, text=text)


@main.route('/user/<name>/update_profile', methods = ['POST','GET'])
@login_required 
def update_user_profile(name): 
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)
    
    form = UpdateProfile() 

    if form.validate_on_submit():
        user.bio = form.bio.data

        user.save_user() 
        return redirect(url_for('.user_profile', name=name))
    
    return render_template('profile/update_profile.html', user=user, form=form)


@main.route('/user/<name>/update/pic')
@login_required 
def update_pic(name): 
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect('main.user_profile', name=name)


@main.route('/upvote/<int:id>')
@login_required 
def upvote(id):
    show_upvotes = Upvote.get_upvotes(id)

    return redirect(url_for('main.index',id=id))


@main.route('/downvote/<int:id>')
@login_required 
def downvote(id):
    show_downvotes = Downvote.get_downvotes(id)

    return redirect(url_for('main.index',id=id)) 