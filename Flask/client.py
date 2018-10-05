import json
import requests

data = {'file_name': '20180830_17:30:22.jpeg', 'file_format': 'jpeg'}
url = "http://0.0.0.0:8000/upload/snapshot/{}"

files = {'files': open('tempFile.txt', 'rb')}
print('\t\trequest at: ' + url.format(data.get('file_name')))
r = requests.post(url.format(data.get('file_name')), files=files)
print(str(r.content, 'utf-8'))
