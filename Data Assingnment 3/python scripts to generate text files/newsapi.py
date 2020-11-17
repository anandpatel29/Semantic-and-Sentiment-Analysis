import pprint
import requests
import re

secret = 'c4de1a6d76774c9687b25a9f10712ce3'

url = 'https://newsapi.org/v2/everything?'

parameters = {
	'q' : 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education',
	'pageSize' : 100,
	'apiKey' : secret
}

response = requests.get(url,params = parameters)
response_json = response.json()

with open('datanews.txt','a+',encoding = 'utf-8') as file:
	for i in response_json['articles']:
		j = i['content']
		j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',str(j))
		j = j.strip()
		datanews = "Author : " + str(i['author']) +" Content : " + j + " Description : " + str(i['description']) +"\n" 
		file.write(datanews)


