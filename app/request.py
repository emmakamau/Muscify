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
    albumImageSmall = chart.get('album',{}).get('cover_small')
    albumImageMedium = chart.get('album',{}).get('cover_medium')
    albumImageLarge = chart.get('album',{}).get('cover_big')
    
    chart_object = Tracks(id,title,link,preview,artistId,artistName,artistAlbum,albumImageSmall,albumImageMedium,albumImageLarge)
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
    cover_medium = album.get('cover_medium')
    cover_big = album.get('cover_big')
    tracklist = getTracksForAlbums(id)

    album_object = Albums(id,title,link,artistId,artistName,cover_medium,cover_big,tracklist)
    album_results.append(album_object)
  return album_results

def getTracksForAlbums(albumsId):
  get_album_tracks_url = 'https://api.deezer.com/album/{}/tracks'.format(albumsId)
  with urllib.request.urlopen(get_album_tracks_url) as url:
    get_chart_data = url.read()
    get_chart_response = json.loads(get_chart_data)
    track_results = None
    if get_chart_response['data']:
      chart_results_list = get_chart_response['data']
      track_results = process_results_tracks(chart_results_list)
  return track_results


# Get chart data by podcast
def getChartPodcasts():
  getchart_url = base_url
  with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        get_chart_response_tracks = get_chart_response.get('podcasts')
        podcast_results = None
        if get_chart_response_tracks['data']:
          chart_results_list = get_chart_response_tracks['data']
          podcast_results = process_results_podcast(chart_results_list)
  return podcast_results

def process_results_podcast(podcast_list):
  podcast_results = []
  for podcast in podcast_list:
    id = podcast.get('id')
    title = podcast.get('title')
    description = podcast.get('description')
    link = podcast.get('link')
    picture_medium = podcast.get('picture_medium')

    podcast_object = Podcasts(id,title,description,link,picture_medium)
    podcast_results.append(podcast_object)
  return podcast_results


# Get chart data by artist
def getChartArtists():
  getchart_url = base_url
  with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        get_chart_response_tracks = get_chart_response.get('artists')
        artist_results = None
        if get_chart_response_tracks['data']:
            chart_results_list = get_chart_response_tracks['data']
            artist_results = process_results_artist(chart_results_list)
  return artist_results

def process_results_artist(artist_list):
  artist_results = []
  for artist in artist_list:
    id = artist.get('id')
    artistName = artist.get('name')
    link = artist.get('link')
    picture_medium = artist.get('picture_medium')
    title = artist.get('title')
    
    artist_object = Artists(id,artistName,link,picture_medium,title)
    artist_results.append(artist_object)
  return artist_results


def getTrack(trackId):
  get_track_url = 'https://api.deezer.com/track/{}'.format(trackId)

  with urllib.request.urlopen(get_track_url) as url:
    track_details_data = url.read()
    track_details_response = json.loads(track_details_data)

    track_object = None

    if track_details_response:
      id = track_details_response.get('id')
      title = track_details_response.get('title')
      link = track_details_response.get('link')
      preview = track_details_response.get('preview')
      artistId = track_details_response.get('artist',{}).get('id')
      artistName = track_details_response.get('artist',{}).get('name')
      artistAlbum = track_details_response.get('album',{}).get('name')
      albumImageSmall = track_details_response.get('album',{}).get('cover_small')
      albumImageMedium = track_details_response.get('album',{}).get('cover_medium')
      albumImageLarge = track_details_response.get('album',{}).get('cover_big')

      print(link)
      track_object= Tracks(id,title,link,preview,artistId,artistName,artistAlbum,albumImageSmall,albumImageMedium,albumImageLarge)
  return track_object

# def getChartPlaylists():
#   getchart_url = base_url
#   with urllib.request.urlopen(getchart_url) as url:
#         get_chart_data = url.read()
#         get_chart_response = json.loads(get_chart_data)
#         get_chart_response_tracks = get_chart_response.get('playlists')
#         playlist_results = None
#         if get_chart_response_tracks['data']:
#             chart_results_list = get_chart_response_tracks['data']
#             playlist_results = process_results_playlist(chart_results_list)
#   return playlist_results

# def process_results_playlist(playlist_list):
#   playlist_results = []
#   for playlist in playlist_list:
#     id = playlist.get('id')
#     link = playlist.get('link')
#     picture_medium = playlist.get('picture_medium')
#     title = playlist.get('title')

#     playlist_object = Playlists(id,link,picture_medium,title)
#     playlist_results.append(playlist_object)
#   return playlist_results


