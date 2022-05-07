from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


# creating db instance 
db = SQLAlchemy() 



def create_app(config_name):
    
    # creating Flask app instance 
    app = Flask(__name__) 
    
    
    # Initializing flask extensions
    db.init_app(app) 


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app 