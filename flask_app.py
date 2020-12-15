import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages

server = Flask(__name__)
server.config.from_object(__name__)
pages = FlatPages(server)
FLATPAGES_EXTENSION = '.md'
server.url_map.strict_slashes = False

@server.route("/")
def index():
    return render_template('index.html', pages=pages)

@server.route("/software.html")
def software():
    return render_template('software.html')

@server.route("/airpollution.html")
def airpollution():
    return render_template('airpollution.html')

if __name__ == '__main__':
    server.run()