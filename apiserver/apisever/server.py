from mainapp import app
from flask_script import Manager
if __name__ == '__main__':
    manager = Manager(app)
    manager.run()