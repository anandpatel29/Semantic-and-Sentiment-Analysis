
import omdb

omdb.set_default('apikey', "d172df2f")
with open('moviedata.txt','a+',encoding = 'utf-8') as file:
	result=omdb.search('Canada') + omdb.search('University') + omdb.search('Moncton') + omdb.search('Halifax') + omdb.search('Toronto') + omdb.search('Vancouver') + omdb.search('Alberta') + omdb.search('Niagara')
	for i in result:
		datanews = "title : " + i['title'] +" year : " + i['year'] + " imdb_id : " + i['imdb_id'] +" type : " + i['type'] +" poster : " + i['poster'] +"\n" 
		file.write(datanews)

