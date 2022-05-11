from app import create_app,db
from flask_script import Manager,Server
from app.models import User
from  flask_migrate import Migrate, MigrateCommand 


# Creating app instance
app = create_app('development')   

# Instantiate Manager class by passing in the app instance 
manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)


# Create a command line argument to tell us how to run our application
# Then, use the add_command method to create a new command 'server' which will launch the app server 
manager.add_command('server',Server)



@manager.shell 
def make_shell_context():
    return dict(app = app,db = db,User = User) 

# Calling the run method on the Manager instance(manager) to run the application 
if __name__ == '__main__': 
    manager.run() 