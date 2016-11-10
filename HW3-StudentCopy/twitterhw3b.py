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

access_token = "2304113095-9WJv6Q4jwUVurnkd0M92OMR9kRm9POFVI23BsCQ"
access_token_secret = "en75xKwsthO2d1mgdtpIdHjkBWV1HaZyw6KkPkDT92BLY"
consumer_key = "sRAjeZ3AQwedfc11WSxH0MS0D"
consumer_secret = "nUHPY4b6PedYd6swMyI3wYf4p9TFdvKg8pESJZH5c98PuEV2Iu"
# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search(input("Please give a Twitter search: "))
count1 = 0
count2 = 0
polarcount = 0
subjectcount = 0
polar = []
subject = []

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
	x = analysis.sentiment.polarity
	polar.append(x)
	for a in polar:
		count1 += 1
	y = analysis.sentiment.subjectivity
	subject.append(y)
	for b in subject:
		count2 += 1


for co in polar:
	polarcount = polarcount + co
for bo in subject:
	subjectcount = subjectcount + bo

polaravg = polarcount / count1
subjectavg = subjectcount / count2
print("\n", polar)
print(subject, "\n")
#You can use sentiment.polarity or sentiment.subjectivity

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.


# tweetz = input("Please do a Twitter search: ")


print("Average subjectivity is ", polaravg)
print("Average polarity is ", subjectavg)
