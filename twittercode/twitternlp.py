import tweepy
import nltk

# Unique code from Twitter
access_token = "2304113095-9WJv6Q4jwUVurnkd0M92OMR9kRm9POFVI23BsCQ"
access_token_secret = "en75xKwsthO2d1mgdtpIdHjkBWV1HaZyw6KkPkDT92BLY"
consumer_key = "w0ibZeUEZoaOO3GdtOar1FZzT"
consumer_secret = "tIwJYo639tvQA3x4z8kw6a4hVNSEAvsWTTWNLGAKSxHrX4BeCI"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

