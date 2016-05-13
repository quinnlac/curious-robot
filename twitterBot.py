import tweepy

import csv
import random

intro = [
"Hey, I've been wondering... ", 
"Just out of curiosity... ",
"I'm stumped right now... ", 
"Hello. A quick question... ",
"I have been pondering on this for a while... ",
"This may be hard to believe but... "]

f = open('newquestions.csv')
csv_f = csv.reader(f)
for row in csv_f:
  print intro[random.randint(0,5)] + row[random.randint(0,49)]

  

class TwitterAPI:
    def __init__(self):
        consumer_key = "9NhQlDMItDVqi7fbbpcaBMTwg"
        consumer_secret = "EhrfQR3CXY3iYkxjnpiyeUuOlRCTjVDOWREyVzHo5LCszeuLjG"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "706865137798483968-HMKspp1yZGlWpRlkSxKHyu7gTEItvdt"
        access_token_secret = "pnZdD4EWCKqHWdfdlndNhrJ9rl3xnIw9ZKFDrdKW7KH2l"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(intro[random.randint(0,5)] + row[random.randint(0,49)])

    #Propose compelling questions