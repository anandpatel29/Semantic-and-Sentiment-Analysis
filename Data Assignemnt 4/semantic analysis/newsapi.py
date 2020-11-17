import pprint
import requests
import re

secret = 'c4de1a6d76774c9687b25a9f10712ce3'

url = 'https://newsapi.org/v2/everything?'

searchwords = ["Canada","University","Dalhousie University","Halifax","Canada Education","Moncton","Toronto"]

j = 1
for word in searchwords:

	parameters = {
		'q' : word,
		'pageSize' : 100,
		'apiKey' : secret
	}

	resp = requests.get(url,params = parameters)
	resp_json = resp.json()

	
	for i in resp_json['articles']:
		outputfilename = "newsapi_" + str(j) + ".txt"
		with open(outputfilename,'w+',encoding = 'utf-8') as outfile:
			datanews = "title : " + str(i['title']) +" Content : " + str(i['content']) + " Description : " + str(i['description']) 
			datanews = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',datanews)
			outfile.write(datanews)
		j=j+1


