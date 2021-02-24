from filesaver import FileSaver
from advancedtweethandler import AdvancedTweetHandler
from playsound import playsound
import tweepy
import threading
import time
class AdvancedListener(tweepy.StreamListener):

    def on_status(self, status): 
        

        # if is in english and fulfills followers threshold
        if self.tweethandler.should_be_analyzed(status):

            
            if self.tweethandler.is_spam(status):
                # print('Spam filtered')
                return

            #checks for keywords and followers count
            if self.tweethandler.is_important(status):
                
                #save to file
                ticker = self.tweethandler.get_category(status=status)
                self.filesaver.save_important_tweet(ticker, status)

            # if self.tweethandler.should_be_printed
            playsound('pop.mp3')
            self.print_tweet(status)



    def print_tweet(self, status):

        username = '@' + status.user.screen_name

        print('\n\n', status.created_at)
        print(username, ' | Fs: ' , status.user.followers_count)

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


    def __init__(self):
        
        super(AdvancedListener, self).__init__()
        print('Listener initialising...')
        # self.followers_threshold = 100
        self.filesaver = FileSaver()
        self.tweethandler = AdvancedTweetHandler()
        self.liable_tweets_read = 0
        self.save_loop_time = 1800
        #start thread and letsketit
        
        t = threading.Thread(target=self.sleep_and_save)
        t.start()
        print('Listener initialised.')


# a = AdvancedListener()