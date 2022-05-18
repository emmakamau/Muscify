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

@main.route('/charts/tracks')
def charts():
    allCharts = getChartTracks()

    return render_template('charts.html',charts=allCharts)

@main.route('/charts/albums')
def albums():
    allAlbums = getChartAlbums()

    return render_template('albums.html',albums=allAlbums)

@main.route('/charts/podcasts')
def podcasts():
    allPodcasts = getChartPodcasts()

    return render_template('podcasts.html',artists=allPodcasts)

@main.route('/charts/artists')
def artists():
    allArtists = getChartArtists()

    return render_template('artists.html',artists=allArtists)