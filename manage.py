from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand #version 2.6.0
from app.models import *

# Creating app instance
app = create_app('development')
app = create_app('test')
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    #Run the unit tests.
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Comment = Comment, Upvote=Upvote,Downvote=Downvote)

if __name__ == '__main__':
    manager.run()
