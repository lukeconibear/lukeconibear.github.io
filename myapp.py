import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return render_template('index.html', pages=pages)

@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)

@app.route("/software.html")
def software():
    return render_template('software.html')

@app.route("/airpollution.html")
def airpollution():
    return render_template('airpollution.html')

#@app.route("/india_sfi_bokeh_plot.html")
#def india_sfi_bokeh_plot():
#    return render_template('india_sfi_bokeh_plot.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
