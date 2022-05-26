# Interacting with Google API to extract trend data
# Dev: Ricky Segura

# Imports
from pytrends.request import TrendReq
import tweepy

# GLOBAL variables
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, 
    CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create API object
API_OBJECT = tweepy.API(auth)

# initialize a new Google Trends Request Object
REQUEST_OBJECT = TrendReq(hl="en-US", tz=360)

# trending searches per region
TRENDING_SEARCHES = REQUEST_OBJECT.trending_searches(pn="united_states")
#TRENDING_SEARCHES[:10]

# Interact with Twitter API to tweet TRENDING_SEARCHES
API_OBJECT.update_status(f"{TRENDING_SEARCHES[:3]}")