import csv, math
Canada_occurence_in_different_doc_count = 0
University_occurence_in_different_doc_count = 0
Dalhousie_University_occurence_in_different_doc_count = 0
Halifax_occurence_in_different_doc_count = 0
Business_occurence_in_different_doc_count = 0
Canada_occurence_in_different_document_array = []

total_doc =700

for i in range(1,total_doc):
	Canada_count_in_a_document = 0
	University_count_in_a_document = 0
	Dalhousie_University_count_in_a_document = 0
	Halifax_count_in_a_document = 0
	Business_count_in_a_document=0
	filename ="newsapi_"+str(i)+".txt"
	with open(filename, 'r', encoding = 'utf-8') as news_data:
		news_article = news_data.readline()
		news_article_words = news_article.split(" ")
		news_article_words = [x.lower() for x in news_article_words]

		for j in range(len(news_article_words)):
			if(news_article_words[j] == 'canada'):
				Canada_count_in_a_document = Canada_count_in_a_document+1
			if(news_article_words[j] == 'university'):
				University_count_in_a_document = University_count_in_a_document+1
			if(j < len(news_article_words) and news_article_words[j] == 'dalhousie' and news_article_words[j+1] == 'university'):
				Dalhousie_University_count_in_a_document = Dalhousie_University_count_in_a_document+1	
			if(news_article_words[j] == 'halifax'):
				Halifax_count_in_a_document = Halifax_count_in_a_document+1
			if(news_article_words[j] == 'business'):
				Business_count_in_a_document = Business_count_in_a_document+1	
			
		if(Canada_count_in_a_document>0):
			Canada_occurence_in_different_doc_count = Canada_occurence_in_different_doc_count+1
			canada_details = str(len(news_article_words)) +","+str(i) +","+str(Canada_count_in_a_document)
			Canada_occurence_in_different_document_array.append(canada_details)
		if(University_count_in_a_document>0):
			University_occurence_in_different_doc_count = University_occurence_in_different_doc_count+1
		if(Halifax_count_in_a_document>0):
			Halifax_occurence_in_different_doc_count = Halifax_occurence_in_different_doc_count+1
		if(Dalhousie_University_count_in_a_document>0):
			Dalhousie_University_occurence_in_different_doc_count = Dalhousie_University_occurence_in_different_doc_count+1
		if(Business_count_in_a_document>0):
			Business_occurence_in_different_doc_count = Business_occurence_in_different_doc_count+1	

Canada_ratio = total_doc/Canada_occurence_in_different_doc_count
University_ratio = total_doc/University_occurence_in_different_doc_count
Dalhousie_University_ratio = total_doc/Dalhousie_University_occurence_in_different_doc_count
Halifax_ratio = total_doc/Halifax_occurence_in_different_doc_count
Business_ratio = total_doc/Business_occurence_in_different_doc_count

with open('_SemanticAnalysis.csv','w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['Total documents',total_doc])
	writer.writerow(['Search Query','Document Containing Term(df)','Total documents(N)/number of  documents  term  appeared (df)','Log10(N/df)'])
	ndf_Canada = str(total_doc)+"/"+str(Canada_occurence_in_different_doc_count)
	ndf_University = str(total_doc) + "/" + str(University_occurence_in_different_doc_count)
	ndf_Dalhousie_University = str(total_doc) + "/" + str(Dalhousie_University_occurence_in_different_doc_count)
	ndf_Halifax = str(total_doc) +"/" + str(Halifax_occurence_in_different_doc_count)
	ndf_Business = str(total_doc) + "/" + str(Business_occurence_in_different_doc_count)
	writer.writerow(['Canada',Canada_occurence_in_different_doc_count, ndf_Canada, str(round(math.log10(Canada_ratio),2))])
	writer.writerow(['University',University_occurence_in_different_doc_count, ndf_University, str(round(math.log10(University_ratio),2))])
	writer.writerow(['Dalhousie University',Dalhousie_University_occurence_in_different_doc_count, ndf_Dalhousie_University, str(round(math.log10(Dalhousie_University_ratio),2))])
	writer.writerow(['Halifax',Halifax_occurence_in_different_doc_count, ndf_Halifax, str(round(math.log10(Halifax_ratio),2))])
	writer.writerow(['Business',Business_occurence_in_different_doc_count, ndf_Business, str(round(math.log10(Business_ratio),2))])
	
Canada_maximum_count = 0
article_no = ''

with open('_SemanticAnalysis2.csv','w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['Term', 'Canada'])
	writer.writerow(['Canada appeared in '+  str(Canada_occurence_in_different_doc_count) + ' documents', 'Total words(m)', 'Frequency(f)'])
	for i in range(Canada_occurence_in_different_doc_count):
		article_details = Canada_occurence_in_different_document_array[i].split(",")
		writer.writerow(["Article #"+ article_details[1], article_details[0], article_details[2]])
		relative_frequency= int(article_details[2])/int(article_details[0])
		if(relative_frequency>Canada_maximum_count):
			Canada_maximum_count=relative_frequency
			article_no = article_details[0]

filename = "newsapi_" +str(article_no) + ".txt"
print(filename)

with open(filename,'r', encoding="utf-8") as file:
	article_data = (file.readline())
	print(article_data)