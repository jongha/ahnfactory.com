import os
import urllib
import jinja2
import webapp2

from flask import Flask

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    template = JINJA_ENVIRONMENT.get_template('views/index.html')
    return template.render({})

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
