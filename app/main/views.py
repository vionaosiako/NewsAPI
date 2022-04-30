from flask import render_template
from ..request import get_sources
from . import main
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
        # Getting popular news
    sources = get_sources()
    return render_template('index.html', sources = sources)