from . import main
from flask import render_template  


# views
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/pitch')
def pitch():
    return render_template('pitches.html')


@main.route('/new_pitch')
def new_pitch():
    return render_template('new_pitch.html')


@main.route('/comment/<int:pitch_id>')
def comment(pitch_id):
    return render_template('comments.html')


@main.route('/user/<name>')
def user_profile(name):
    return render_template('profile/user_profile.html')


@main.route('/user/<name>/update_profile')
def update_user_profile(name): 
    return render_template('profile/update_profile.html')


@main.route('/user/<name>/update/pic')
def update_pic(name): 
    return render_template('main.user_profile')


@main.route('/upvote/<int:id>')
def upvote(id):
    pass 


@main.route('/downvote/<int:id>')
def downvote(id):
    pass 