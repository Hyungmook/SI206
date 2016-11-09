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
consumer_secret = "	nUHPY4b6PedYd6swMyI3wYf4p9TFdvKg8pESJZH5c98PuEV2Iu"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

def tweet_image(url, message):
    api = tweepy.API(auth)
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


url = "http://www.rd.com/wp-content/uploads/sites/2/2016/04/05-cat-wants-to-tell-you-bathing-myself.jpg"
message = "Testing for a class using APIs"
tweet_image(url, message)
public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)