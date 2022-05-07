from flask import Flask



def create_app(config_name):
    
    # creating Flask app instance 
    app = Flask(__name__)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app 