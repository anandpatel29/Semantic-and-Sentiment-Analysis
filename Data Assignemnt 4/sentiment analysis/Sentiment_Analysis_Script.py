import csv

positive_dict = {}
negative_dict = {}

positive_list=[]
with open('Positive Words from online sources.txt') as positivefile:
  positive_list = [positiveword.strip() for positiveword in positivefile.readlines()]

negative_list=[]
with open('Negative Words from online sources.txt',encoding="ISO-8859-1") as negativefile:
  negative_list = [negativeword.strip() for  negativeword in negativefile.readlines()]


list_of_tweets = []
with open('tweet_data.txt') as inputfile:
  tweet = [x.strip() for x in inputfile.readlines()]
  for line in tweet:
    line = line.replace('\n','')
    line = line.replace('\r','')
    line = line.replace('Tweet:','')
    list_of_tweets.append(line)


list_bag_of_words = []
with open('sentiment_analysis.csv','w') as outfile:
  outputwriter = csv.writer(outfile, lineterminator = '\n')
  outputwriter.writerow(['Tweet','Message','Match','Polarity'])
  for i in range(len(list_of_tweets)):
      bag_of_words = {}
      words_in_tweet = list_of_tweets[i].split(" ")
      for word_in_tweet in range(len(words_in_tweet)):
        key = words_in_tweet[word_in_tweet]
        key = key.lower()
        if key in bag_of_words.keys():
          bag_of_words[key] = bag_of_words[key] + 1
          
        else:
          bag_of_words[key] = 1
      
      list_bag_of_words.append(bag_of_words)
      count_positive=0
      count_negative=0
      count_neutral=0
      outputpolarity="neutral"
      list_match_words=""
      list_positive_match_words =""
      list_negative_match_words = ""
      for list_keys in bag_of_words.keys():
        if list_keys in positive_list:
          count_positive=count_positive+1
          if list_keys in positive_dict.keys():
            positive_dict[list_keys] = positive_dict[list_keys] + 1
          else:
            positive_dict[list_keys] = 1
          list_positive_match_words=list_positive_match_words + list_keys +","
        elif list_keys in negative_list:
          count_negative=count_negative+1
          if list_keys in negative_dict.keys():
            negative_dict[list_keys] = negative_dict[list_keys] + 1
          else:
            negative_dict[list_keys] = 1
          list_negative_match_words=list_negative_match_words + list_keys +","
        else:
          count_neutral=count_neutral+1   
      if(count_positive>count_negative):
        outputpolarity="positive"  
        list_match_words=list_positive_match_words
      elif(count_positive<count_negative):
        outputpolarity="negative"  
        list_match_words=list_negative_match_words
      else:
         list_match_words="NONE," 
      outputwriter.writerow([i,list_of_tweets[i],list_match_words[:-1],outputpolarity]);   

with open('Positive_words_count.csv','w') as file:
  positive = csv.writer(file, lineterminator = '\n')
  positive.writerow(['words','Count'])
  for list_keys in positive_dict.keys():
    positive.writerow([list_keys, positive_dict[list_keys]])


with open('Negative_words_count.csv','w') as file:
  negative = csv.writer(file, lineterminator = '\n')
  negative.writerow(['words','Count'])
  for list_keys in negative_dict.keys():
    negative.writerow([list_keys, negative_dict[list_keys]])    



