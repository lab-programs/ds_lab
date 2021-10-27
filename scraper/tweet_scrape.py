"""
!pip3 install snscrape
!rm -rf filename.txt
!wget https://raw.githubusercontent.com/tezz-io/ds_lab/main/output/filename.txt
"""
f1 = open("filename.txt")
s = f1.read().split("\n")

import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

tweets1 = {}

def increment_date(date):
  year = int(date[0:4])
  month = int(date[5:7])
  date = int(date[8:])
  date += 1
  if month in [1, 3, 5, 7, 8, 10, 12] and date > 31:
    date = 1
    month += 1
  if month in [4, 6, 9, 11] and date > 30:
    date = 1
    month += 1
  if month == 2 and year % 4 == 0 and date > 29:
    date = 1
    month += 1
  if month == 2 and year % 4 != 0 and date > 28:
    date = 1
    month += 1
  if month > 12:
    month = 1
    year += 1

  x = ""
  x += str(year) + '-'
  if month < 10:
    x += '0'
  x += str(month) + '-'
  if date < 10:
    x += '0'
  x += str(date)

  return x


for x in s:
  x = str(x)
  x = x[0:4] + "-" + x[4:6] + "-" + x[6:]
  print(x, increment_date(x))

  # Creating list to append tweet data to
  tweets_list2 = {}

  # Using TwitterSearchScraper to scrape data and append tweets to list
  for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#mannkibaat since:'+x+' until:'+increment_date(x)).get_items()):
      if i>1000:
          break
      tweets_list2[tweet.id] = tweet.content
  tweets1[x] = tweets_list2  
  # print(tweets_list2)
    
# print(tweets1)
# Creating a dataframe from the tweets list above
f = open("tweets.json","w+")
json.dump(tweets1,f,ensure_ascii = True)
