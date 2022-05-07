from app import create_app
from flask_script import Manager, Server 

# Creating app instance
app = create_app('development') 



# Instantiate Manager class by passing in the app instance
manager = Manager(app)


manager.add_command('server',Server)  

@manager.shell 
def make_shell_context():
    return dict(app = app) 

# Calling the run method on the Manager instance(manager) to run the application 
if __name__ == '__main__': 
    manager.run()  