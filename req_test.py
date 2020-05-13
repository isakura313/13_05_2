import requests

payloads = {'page':2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payloads)
print(r.text)