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