import tweepy

from playsound import playsound
from timeit import default_timer as timer
from datetime import datetime

from filesaver import FileSaver
from tweethandler import TweetHandler

class BasicListener(tweepy.StreamListener):

    def on_status(self, status): 
        
        #if contains spam
        if self.tweethandler.contains_spam(status.text):
            print('Tweet filtered')
            return


        #if meets requirements to print
        if status.user.followers_count >= self.threshold and status.lang == 'en': 

            self.liable_tweets_read += 1
            self.check_time()


            #play a sound and console goes brr
            playsound('pop.mp3')
            print('\n------------')
            print(status.created_at)
            print('@',status.user.screen_name,' | Fs: ', status.user.followers_count)

            try:      
                print(status.extended_tweet["full_text"])
            except AttributeError:
                print(status.text)
                
            print('------------')


            # save important tweets to file for later analysis or some shit XD
            if self.tweethandler.check_if_important(status):
                print('Important tweet found')
                self.filesaver.save_important(status)


    def on_error(self, status_code):
        print('brrr ', status_code)
        return False #drop connection



    def check_time(self):
        # to-do comeup with sth better .-.
        self.end = timer()

        if (self.end - self.start )>= 900: #at least 900s elapsed
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")


            self.filesaver.save_mentions(current_time, self.liable_tweets_read)

            #reset counter and timer
            self.liable_tweets_read = 0
            self.start = timer()
        


    # def set_follower_threshold(self, follower_count):
    #     self.threshold = follower_count
    #     print ('Self threshold set to', self.threshold)


    def setup_shit(self, follower_threshold):
        
        print('Listener init innit me boi')
        self.threshold = follower_threshold
        self.start = timer()
        self.filesaver = FileSaver()
        self.tweethandler = TweetHandler()
        self.liable_tweets_read = 0