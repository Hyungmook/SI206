# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
import sys



# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Sets a variable with tweepy API. 
api = tweepy.API(auth)


# Receives an input from the user
public_tweets = api.search(input("Please give a Twitter search: "))
count = 0 #Count for getting the average
polarcount = 0 #Counts every polar (adds the polarity)
subjectcount = 0 #Counts every subject (adds the subjectivity)

# Code that was provided by GSI to allow tweets to be printed
def uprint(*objects, sep='', end='\n', file=sys.stdout):
	enc = file.encoding
	if enc == 'UTF-8':
		print(*objects, sep=sep, end=end, file=file)
	else:
		f = lambda obj: str(obj).encode(enc, errors='backslashreplace')
		print(*map(f, objects), sep=sep, end=end, file=file)


for tweet in public_tweets:
	uprint(tweet.text)
	analysis = TextBlob(tweet.text)
	#Receives the polarity counts
	polarcount += analysis.sentiment.polarity
	#Receives the subjectivity counts
	subjectcount += analysis.sentiment.subjectivity
	count += 1

#Finding the average for both polarity and subjectivity
polaravg = polarcount / count
subjectavg = subjectcount / count

#You can use sentiment.polarity or sentiment.subjectivity

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.


# tweetz = input("Please do a Twitter search: ")


print("Average subjectivity is ", subjectavg)
print("Average polarity is ", polaravg)
