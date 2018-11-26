import urllib.request, json
import contextlib
from datetime import datetime
import time


def call(url):
    req = urllib.request.Request(url)
    with contextlib.closing(urllib.request.urlopen(req)) as response:
        request = response.read()
        request = request.decode("utf-8").replace("'", '"')
        data = json.loads(request)
    return data


if __name__ == '__main__':
	timeStop = "2018-11-12 01:00:00"
	timeStart = "2018-10-29 01:00:00"
	tStop = datetime.strptime(timeStop, "%Y-%m-%d %H:%M:%S")
	tIt = datetime.strptime(timeStart, "%Y-%m-%d %H:%M:%S")
	timestamp = int(tIt.timestamp())
	stopToken = True
	wikistamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')

	out_file = open('wikiExtendedData.json', 'w')

	while(stopToken):
	    url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=recentchanges&rcprop=ids%7Csizes%7Cfrcshow=!bot%7Clags%7Cuserid%7Ctimestamp&rclimit=500&rcstart={wikistamp}&rcdir=newer'
	    print(url)

	    data = call(url)
	    content = data['query']['recentchanges']
	    lastTime = content[-1]['timestamp']
	    tCurrent = datetime.strptime(lastTime, "%Y-%m-%dT%H:%M:%SZ")

	    content_str = '\n'.join(str(v) for v in content)
	    content_str = content_str.replace('\'',r'"')
	    out_file.write(content_str)
	    timestamp = int(tCurrent.timestamp()) + 3601
	    wikistamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')

	    if tCurrent >= tStop:
	         break

	out_file.close()
