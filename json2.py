import urllib.request, urllib.parse, urllib.error
import json

data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1559904.json')


info = json.loads(data.read().decode())
sum = 0
for item in info["comments"]:
    # print('Name', item['name'])
    sum += item['count']

print(sum)
