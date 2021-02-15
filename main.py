import tweepy

from basiclistener import BasicListener
import constants

def main():

    tickers = ['XLM'] # $NANO $XRP $ADA $DOT    $DOGE woof 
    # musk = '44196397';
    # tweet_count = 10


    auth = tweepy.OAuthHandler(constants.API_KEY, constants.API_KEY_SECRET)
    auth.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser() )


    
    # status = api.user_timeline(user_id=musk, count=tweet_count)
    # for i in range(tweet_count):
    #     tweet = status[i]
    #     print( tweet['created_at'])
    #     print( tweet['id'])
    #     print( tweet['text'])
    #     print('\n')


    basic_listener = BasicListener()
    # basic_listener.set_follower_threshold(100)
    basic_listener.setup_shit(100)


    stream = tweepy.Stream(auth=api.auth, listener=basic_listener)
    stream.filter(track=tickers, is_async=True)




main()
    