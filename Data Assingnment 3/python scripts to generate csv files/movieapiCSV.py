import omdb
import csv
omdb.set_default('apikey', "d172df2f")

fields=['title','year','imdb_id','type','poster']
with open('moviedataCSV.csv','w+',newline='') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=fields)
	writer.writeheader()
	result=omdb.search('Canada') + omdb.search('University') + omdb.search('Moncton') + omdb.search('Halifax') + omdb.search('Toronto') + omdb.search('Vancouver') + omdb.search('Alberta') + omdb.search('Niagara')
	for i in result:
		data={}
		data["title"] = i['title']
		data["year"] = i['year']
		data["imdb_id"] = i['imdb_id']
		data["type"] = i['type']
		data["poster"] = i['poster']
		writer.writerow(data)