from tweepy import API
from tweepy import cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re
import csv


ACCESS_TOKEN = "323893118-5CPg5GwweNrmiXIu8Kvfm2dUhlGwCPyEuMkXVsim"
ACCESS_TOKEN_SECRET = "ws0CTJkMR9jhrWwN8BSMCiwUKRlVicH34M03ndW1D511G"
CONSUMER_KEY = "B8gjHWljfi8rSxCoXFZSs9FZs"
CONSUMER_KEY_SECRET = "hJDULA7HFgNnojyMJ3sMQFhTaGfxK42LIakrt31UrqzZJKdyen"

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY ,CONSUMER_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():

    def __init__(self):
        self.twitterauthenticator = TwitterAuthenticator()

    def stream_tweets(self, tweet_filename, hashtag_list):
        listener = TwitterListener(tweet_filename)
        auth = self.twitterauthenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track = hashtag_list)


class TwitterListener(StreamListener):

    def __init__(self, tweet_filename):
        self.tweet_filename = tweet_filename

    def on_data(self, data):
        try:
            i = 0
            fields=['id_str','text','created_at','place']
            with open('dataCSV.csv',mode='a+',newline='') as tf:
                writer = csv.DictWriter(tf, fieldnames=fields)
                if(i<100):
                    data1 = {}
                    i=i+1
                    datajson = json.loads(data)
                    j = datajson["text"]
                    j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',j)
                    j = j.strip()
                    idstr = datajson["id_str"]
                    datecreated = datajson["created_at"]
                    loc = datajson["place"]
                    data1["id_str"] = idstr
                    data1["text"] = j
                    data1["created_at"] = str(datecreated)
                    data1["place"] = str(loc)
                    writer.writerow(data1)
            return True
        except BaseException as e:
            print("Error on data : %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

    pass
if __name__ == '__main__':
    hashtag_list = ['Canada, University, Dalhousie University, Halifax, Canada Education']
    tweet_filename = "data1.csv"

    twitterStreamer = TwitterStreamer()
    twitterStreamer.stream_tweets(tweet_filename, hashtag_list)