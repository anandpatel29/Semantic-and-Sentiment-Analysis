import requests
import re

with open("moviedata.txt" , 'r' , encoding = 'utf-8') as file:
	while True:
		line = file.readline()
		if not line:
			break
		start = re.search(r"imdb_id : ", line).end()
		imdbId = line[start:start+9] 
		url = "http://www.omdbapi.com/?i="+ imdbId +"&apikey=d172df2f"
		resp = requests.get(url)
		with open("moviedetails.txt" , 'a' , encoding = 'utf-8') as outfile:
			data = "imdb_id : " + imdbId + " Rating : " + resp.json()["Rated"]+" Genre : " + resp.json()["Genre"] + " Plot : " + resp.json()["Plot"]+"\n"
			outfile.write(data)

