from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail 


# creating db instance        
db = SQLAlchemy()

# creating bootstrap instance
bootstrap = Bootstrap() 

# creating login_manager instance
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# creating photos instance
photos = UploadSet('photos',IMAGES)

# creating mail instance 
mail = Mail()


def create_app(config_name):

    # creating Flask app instance 
    app = Flask(__name__) 
    
    
    # Initializing flask extensions
    db.init_app(app) 
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name]) 
    
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    
    # configure UploadSet
    configure_uploads(app,photos) 


    return app 