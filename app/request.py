import urllib.request,json
from . models import Chart

base_url = 'https://api.deezer.com/chart/tracks'


def getChartTracks():
    getchart_url = base_url
    with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        get_chart_response_tracks = get_chart_response.get('tracks')
        chart_results = None
        if get_chart_response_tracks['data']:
            chart_results_list = get_chart_response_tracks['data']
            chart_results = process_results(chart_results_list)
    return chart_results

def process_results(chart_list):
  chart_results = []
  for chart in chart_list:
    # artistId,artistName,albumId
    # language = books.get('volumeInfo',{}).get('language')
    id = chart.get('id')
    title = chart.get('title')
    link = chart.get('link')
    preview = chart.get('preview')
    artistId = chart.get('artist',{}).get('id')
    artistName = chart.get('artist',{}).get('name')
    artistAlbum = chart.get('album',{}).get('id')

    chart_object = Chart(id,title,link,preview,artistId,artistName,artistAlbum)
    chart_results.append(chart_object)
  return chart_results






