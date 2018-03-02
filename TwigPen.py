# TwigPen
v=0.0

# Intended to be imported as a module in other scripts, not a standalone application. Crucially, sets up the auth tokens.

# From http://testdawg.com/index.php/2017/02/20/automatically-post-tweets-using-python-twitter-api/

# Import a Twitter module:
from twython import Twython
import random

# Prepare the keys to connect to Twitter:
f = open('twitter_tokens.txt', 'r')
tokens = f.readlines()
TWITTER_APP_KEY = tokens[0].rstrip('\n')
TWITTER_APP_KEY_SECRET = tokens[1].rstrip('\n')
TWITTER_ACCESS_TOKEN = tokens[2].rstrip('\n')
TWITTER_ACCESS_TOKEN_SECRET = tokens[3].rstrip('\n')
f.close()

# Setup the token variables:
t = Twython(app_key=TWITTER_APP_KEY,
	app_secret=TWITTER_APP_KEY_SECRET,
	oauth_token=TWITTER_ACCESS_TOKEN,
	oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)


# COMMANDS:

# Post something:
def postsomething(sometext):
	t.update_status(status=sometext)
