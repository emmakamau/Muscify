from . import main
from flask import render_template
from ..request import *

@main.route('/')
def index():
    allCharts = getchart()

    return render_template('index.html',charts=allCharts)