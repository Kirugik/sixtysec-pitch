from . import main
from flask import render_template  


# views
@main.route('/')
def index():
    pass 


@main.route('/pitch')
def pitch():
    pass 


@main.route('/new_pitch')
def new_pitch():
    pass

@main.route('/comments/<int:pitch_id>')
def comments(pitch_id):
    pass 


@main.route('/user/<name>')
def user_profile(name):
    pass 


@main.route('/user/<name>/update_profile')
def update_user_profile(name): 
    pass 


@main.route('/upvote/<int:id>')
def upvote(id):
    pass 


@main.route('/downvote/<int:id>')
def downvote(id):
    pass 