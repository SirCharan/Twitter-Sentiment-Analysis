#Import Necessary Libraries
import tweepy
import vaderSentiment
import nltk
import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

#Make your own acces to these keys, hidden for security purposes
consumer_key = '############'
consumer_secret = '############'
access_token = '############'
access_token_secret = '############'

#Authorize using these keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Searcha specifc word/person/anything you want
search_term=input("Enter Word-")
tweets = api.search(search_term, count=50)
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

#Save and display the new procured tweets
data.to_csv(r"")
display(data.head(10))
print(tweets[0].created_at)

sid = SentimentIntensityAnalyzer()

listy = []

#Perform Sentiment Analysis and Display results
for index, row in data.iterrows():
    ss = sid.polarity_scores(row["Tweets"])
    listy.append(ss)
    
se = pd.Series(listy)
data['polarity'] = se.values

display(data.head(100))
