import tweepy as tw
import pandas as pd
import csv
import re

ACCESS_TOKEN = "323893118-5CPg5GwweNrmiXIu8Kvfm2dUhlGwCPyEuMkXVsim"
ACCESS_TOKEN_SECRET = "ws0CTJkMR9jhrWwN8BSMCiwUKRlVicH34M03ndW1D511G"
CONSUMER_KEY = "B8gjHWljfi8rSxCoXFZSs9FZs"
CONSUMER_KEY_SECRET = "hJDULA7HFgNnojyMJ3sMQFhTaGfxK42LIakrt31UrqzZJKdyen"

auth = tw.OAuthHandler(CONSUMER_KEY ,CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth, wait_on_rate_limit=True)
date_since = "2019-06-16"

hashtag_list = 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education'

tweets = tw.Cursor(api.search,
              q=hashtag_list,
              lang="en",
              since=date_since).items(3000)

fields=['id_str','text','created_at','place']

with open('dataCSV.csv',mode='w+',newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    for i in tweets:
        data = {}
        j = i.text
        j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',j)
        j = j.strip()
        data["id_str"] = i.id_str
        data["text"] = j
        data["created_at"] = str(i.created_at)
        data["place"] = str(i.place)
        writer.writerow(data)