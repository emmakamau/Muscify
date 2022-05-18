import urllib.request,json
from . models import *

base_url = 'https://api.deezer.com/chart'

# Get chart data by track
def getChartTracks():
    getchart_url = base_url
    with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        get_chart_response_tracks = get_chart_response.get('tracks')
        track_results = None
        if get_chart_response_tracks['data']:
            chart_results_list = get_chart_response_tracks['data']
            track_results = process_results_tracks(chart_results_list)
    return track_results

def process_results_tracks(track_list):
  track_results = []
  for chart in track_list:
    id = chart.get('id')
    title = chart.get('title')
    link = chart.get('link')
    preview = chart.get('preview')
    artistId = chart.get('artist',{}).get('id')
    artistName = chart.get('artist',{}).get('name')
    artistAlbum = chart.get('album',{}).get('id')
    albumImage = chart.get('album',{}).get('cover_medium')
    
    chart_object = Tracks(id,title,link,preview,artistId,artistName,artistAlbum,albumImage)
    track_results.append(chart_object)
  return track_results

# Get chart data by albums
def getChartAlbums():
   getchart_url = base_url
   with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        get_chart_response_tracks = get_chart_response.get('albums')
        album_results = None
        if get_chart_response_tracks['data']:
            chart_results_list = get_chart_response_tracks['data']
            album_results = process_results_albums(chart_results_list)
   return album_results

def process_results_albums(albums_list):
  album_results = []
  for album in albums_list:
    id = album.get('id')
    title = album .get('title')
    link = album.get('link')
    artistId = album.get('artist',{}).get('id')
    artistName = album.get('artist',{}).get('name')
    albumImage = album.get('album',{}).get('cover_medium')

    album_object = Albums(id,title,link,artistId,artistName,albumImage)
    album_results.append(album_object)
  return album_results

# Get chart data by podcast
def getChartPodcasts():
  podcast_results = None
  return podcast_results

def process_results_podcast(podcast_list):
  podcast_results = []
  return podcast_results


# Get chart data by artist
def getChartArtists():
  artist_results = None
  return artist_results

def process_results_artist(artist_list):
  artist_results = []
  return artist_results

