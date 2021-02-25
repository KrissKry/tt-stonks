import tweepy

from basiclistener import BasicListener
from advancedlistener import AdvancedListener
import constants
from util import load_tickers

def main():

    tickers = load_tickers()
    # musk = '44196397';


    auth = tweepy.OAuthHandler(constants.API_KEY, constants.API_KEY_SECRET)
    auth.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser() )



    # basic_listener = BasicListener()
    # basic_listener.setup_shit(100)
    listener = AdvancedListener()

    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=tickers, is_async=True)


main()    