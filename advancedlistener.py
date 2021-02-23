from filesaver import FileSaver
from advancedtweethandler import AdvancedTweetHandler
from playsound import playsound
import tweepy
import threading
import time
class AdvancedListener(tweepy.StreamListener):

    def on_status(self, status): 
        
        if tweethandler.is_spam(status):
            return

        # if !self.fulfills_threshold():
        #     return


        if self.tweethandler.is_important(status):
            print('Important tweet found')
            print('to-do saving important tweets to proper files')
            ticker = self.tweethandler.get_category(status=status)
            self.filesaver.save_important_tweet(ticker, status)
            # self.filesaver.save_important(status)


        if self.tweethandler.should_be_printed(status):
            playsound('pop.mp3')
            print('\n\n', status.created_at)
            print('@',status.user.screen_name,' | Fs: ', status.user.followers_count)

            try:      
                print(status.extended_tweet["full_text"])
            except AttributeError:
                print(status.text)
                
            print('------------')
        



    def on_error(self, error_code):

        #too many api calls
        if error_code == 401:
            print('Too many API calls ;-;')
            return False
        elif error_code == 420:
            print('AUTH Failed. Blaze it.')
            return False

            #sprawdzic z ktorych bledow mozna sie podniesc
        else:
            return True


    def sleep_and_save(self):

        while True:
            # do shit
            time.sleep(self.save_loop_time)
            #self.filesaver.save_stuff()
            #to-do


    def fulfills_threshold(self, status):
        return self.followers_threshold >= status.user.followers_count


    def __init__(self):
        
        super(AdvancedListener, self).__init__()
        # self.followers_threshold = 100
        self.filesaver = FileSaver()
        self.tweethandler = AdvancedTweetHandler()
        self.liable_tweets_read = 0
        self.save_loop_time = 1800
        #start thread and letsketit
        
        t = threading.Thread(target=self.sleep_and_save)
        t.start()



a = AdvancedListener()