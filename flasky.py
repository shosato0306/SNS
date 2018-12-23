import os
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """flask The shell command invokes this function
    with a shell_context_processor decorator every time it starts up""" 
    print("flasky.make_shell_context")
    return dict(db=db, User=User, Follow=Follow,
                Role=Role, Permission=Permission, Post=Post)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

