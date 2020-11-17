import requests
import re
import csv

fields=['imdb_id','Rating','Genre','Plot']
with open("moviedata.txt" , 'r' , encoding = 'utf-8') as file:
	i=0
	while True:
		line = file.readline()
		if not line:
			break
		start = re.search(r"imdb_id : ", line).end()
		imdbId = line[start:start+9] 
		url = "http://www.omdbapi.com/?i="+ imdbId +"&apikey=d172df2f"
		resp = requests.get(url)
		with open("moviedetailsCSV.csv" , 'a' , newline='') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames=fields)
			if i==0:
				writer.writeheader()
				i+=1
			data={}
			data["imdb_id"]= imdbId
			data["Rating"] = resp.json()["Rated"]
			data["Genre"] = resp.json()["Genre"]
			data["Plot"] = resp.json()["Plot"]
			writer.writerow(data)