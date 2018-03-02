import TwigPen
tweettext = input('Tweet something: ')
if tweettext:
	TwigPen.postsomething(tweettext)
	print('\nTweeted.')
elif not tweettext:
	print('\nNothing to post.')
