import pprint
import requests
import re
import csv

secret = 'c4de1a6d76774c9687b25a9f10712ce3'

url = 'https://newsapi.org/v2/everything?'

parameters = {
	'q' : 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education',
	'pageSize' : 100,
	'apiKey' : secret
}

response = requests.get(url,params = parameters)
response_json = response.json()
fields=['author','content','description']
with open('datanewsCSV.csv','w+',newline='') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=fields)
	writer.writeheader()
	for i in response_json['articles']:
		data = {}
		j = i['content']
		j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',str(j))
		j = j.strip()
		data["author"] = str(i['author'])
		data["content"] = j
		data["description"] = str(i['description'])
		writer.writerow(data)
