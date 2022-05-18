import urllib.request,json
from . models import Chart

base_url = 'https://api.deezer.com/chart/tracks'


def getchart():
    getchart_url = base_url
    with urllib.request.urlopen(getchart_url) as url:
        get_chart_data = url.read()
        get_chart_response = json.loads(get_chart_data)
        chart_results = None
        if get_chart_response['tracks']:
            chart_results_list = get_chart_response['tracks']
            chart_results_list = process_results(chart_results_list)
    return chart_results

def process_results(chart_list):
  allcharts = []
  for chart in chart_list:
    id = chart.get('id')
    title = chart.get('title')
    link = chart.get('link')
    preview = chart.get('preview')

    chart_object = Chart(id,title,link,preview)
    allcharts.append(chart_object)
    print(allcharts)
  return allcharts






