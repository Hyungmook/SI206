import tweepy
import json

# Unique code from Twitter
access_token = "2304113095-9WJv6Q4jwUVurnkd0M92OMR9kRm9POFVI23BsCQ"
access_token_secret = "en75xKwsthO2d1mgdtpIdHjkBWV1HaZyw6KkPkDT92BLY"
consumer_key = "w0ibZeUEZoaOO3GdtOar1FZzT"
consumer_secret = "tIwJYo639tvQA3x4z8kw6a4hVNSEAvsWTTWNLGAKSxHrX4BeCI"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


