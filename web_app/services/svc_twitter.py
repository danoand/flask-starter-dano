import tweepy
import os

TWITTER_API_KEY             = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET          = os.getenv("TWITTER_API_SECRET")
TWITTER_API_TOKEN           = os.getenv("TWITTER_API_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_API_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# Create a Twitter api client object
api = tweepy.API(auth)

# Execute the service
if __name__ == "__main__":
    print("INFO: fetch data from the Twitter API")

    # Set a Twitter user on which to fetch data
    user = api.get_user("@bigdaddygeo")

    print("INFO: user data for: @bigdaddygeo: ", user)
