from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import *

@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)

@main.route('/discover')
def discover():
   title='Discover'

   return render_template('discover.html',title=title)

@main.route('/charts')
def charts():
    allCharts = getChartTracks()

    return render_template('charts.html',charts=allCharts)
