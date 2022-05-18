<<<<<<< HEAD
from flask import render_template,request,redirect,url_for,abort
from . import main

@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)

@main.route('/discover')
def discover():
   title='Discover'

   return render_template('discover.html',title=title)
=======
from . import main
from flask import render_template
from ..request import *

@main.route('/')
def index():
    allCharts = getchart()

    return render_template('index.html',charts=allCharts)
>>>>>>> 7a05275dc11ba247bf01b1b05f3344a960b14366
