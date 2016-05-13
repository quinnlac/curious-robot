import time
import tweepy
from time import sleep

import csv
import random


print "running code"

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

consumer_key = '9NhQlDMItDVqi7fbbpcaBMTwg'
consumer_secret = 'EhrfQR3CXY3iYkxjnpiyeUuOlRCTjVDOWREyVzHo5LCszeuLjG'
access_token = '706865137798483968-HMKspp1yZGlWpRlkSxKHyu7gTEItvdt'
access_token_secret = 'pnZdD4EWCKqHWdfdlndNhrJ9rl3xnIw9ZKFDrdKW7KH2l'

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)
myBot = api.get_user(screen_name = '@CuriosityRobo')
# api.create_list('Sorry for adding you', mode="public", description = 'I had to add you sorry :(')
	
# above retrieved from tweepy list method documentation
# above sets up API information


f = open('newquestions.csv')
csv_f = csv.reader(f)
for row in csv_f:
  print row[random.randint(0,45)]

# Cycle will allow action to be performed every 3600 seconds
# CuriosityBot will look for 3 posts that have #question, CuriosityBot 
# will then retweet these posts as well as post a question of his own in response
def cycle(): 
	for tweet in tweepy.Cursor(api.search, q= "#question").items(3) :
		try:
			if tweet.user.id == myBot.id:
				# No need to retweet ourselves!
				continue
			print("Found tweet by: @" + tweet.user.screen_name)
			# tweet is pointed to tweet itself, however .user and .screen_name point those too
			# below is troubleshooting
			if(tweet.retweeted == False) or (tweet.favorited == False):
				tweet.retweet()
				api.update_status("@"+ tweet.user.screen_name + " " + intro[random.randint(0,5)] + row[random.randint(0,49)], in_reply_to_status_id = tweet.user.id)
			#	tweet.favorite()
			#	print('retweet and favorited the tweet')
			if(tweet.user.following == False):
				tweet.user.follow()
				print('Follow the user')
		except tweepy.TweepError as e:
			print(e.reason)
			sleep(10)
			continue
		except StopIteration:
			break
		time.sleep(3600)

while True:
	cycle()

# search for a certain word or hashtag in q
# it will return a bunch of tweets
# can specify timeframe/language of tweet retreival with q= 'x', lang="en" 
# items = number of tweets 

