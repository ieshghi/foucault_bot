import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("qpgHso8iCRecnwJrmsHSOuBqv", 
    "iUAWohrX2Uema8VneS3UnONzpolv1YKJ8qK6Wblq6RxTf594Pr")
auth.set_access_token("1297379680513863680-OlT6wq6NPKaAdSacHrbb3UQsa2cK4D", 
    "7J0StHUWDxxM246jBHKRoXzotJCTvFhWWuDDg4bcRXB6c")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
