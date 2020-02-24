from flask_frozen import Freezer
from flask_app import server

freezer = Freezer(server)

if __name__ == '__main__':
    freezer.freeze()
