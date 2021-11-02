import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

# Creating list to append tweet data to
tweets_list2 = {}

# Using TwitterSearchScraper to scrape data and append tweets to list.
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#mannkibaat since:2021-09-26 until:2021-09-27').get_items()):
    if i>1000:
        break
    tweets_list2[tweet.id]  = tweet.content
    
# Creating a dataframe from the tweets list above
f = open("tweets.json","w+")
json.dump(tweets_list2,f,ensure_ascii = True)

