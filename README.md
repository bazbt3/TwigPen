## My Twitter app description:
"A multi-purpose Python module for inclusion in my other scripts."

Sets up Twitter auth tokens and provides a 'wrapper' for Twython.

### Prerequisites:
* [twython](https://github.com/ryanmcgrath/twython), installed on shared hosting by `pip3.6 install --user twython`
* A text file in which are stored your 4 Twitter auth tokens, each on a separate line. Opened in order with code *like* this:    
```
f = open('twitter_tokens.txt', 'r')
tokens = f.readlines()
TWITTER_APP_KEY = tokens[0].rstrip('\n')
TWITTER_APP_KEY_SECRET = tokens[1].rstrip('\n')
TWITTER_ACCESS_TOKEN = tokens[2].rstrip('\n')
TWITTER_ACCESS_TOKEN_SECRET = tokens[3].rstrip('\n')
f.close()
```

Example script `test_twigpen.py` in this repo:    
```
import TwigPen
tweettext = input('Tweet something: ')
if tweettext:
	TwigPen.postsomething(tweettext)
	print('\nTweeted.')
elif not tweettext:
	print('\nNothing to post.')
```
