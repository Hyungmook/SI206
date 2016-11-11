# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy
import requests
# Unique code from Twitter
access_token = "2304113095-9WJv6Q4jwUVurnkd0M92OMR9kRm9POFVI23BsCQ"
access_token_secret = "en75xKwsthO2d1mgdtpIdHjkBWV1HaZyw6KkPkDT92BLY"
consumer_key = "sRAjeZ3AQwedfc11WSxH0MS0D"
consumer_secret = "nUHPY4b6PedYd6swMyI3wYf4p9TFdvKg8pESJZH5c98PuEV2Iu"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
# Sets a variable with tweepy API 
api = tweepy.API(auth)
# Gets my image
img = "tiny_cat_12573_8950.jpg"
# Uploads the image with the caption into Twitter
api.update_with_media(img, status="#UMSI-206 #Proj3")


