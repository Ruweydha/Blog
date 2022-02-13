from flask import render_template
from . import main
from ..requests import random

@main.route('/')
def index():
    
    random_quote = random()

    return render_template('index.html', random = random_quote)