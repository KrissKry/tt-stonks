from datetime import datetime

class FileSaver():

    def save_mentions(self, timestamp, count):
        f = open("mentions.txt","a")

        wr_str = timestamp + ' ' + str(count) + '\n'

        f.write(wr_str)
        f.close()


    #define definition of an important tweet?
    def save_important(self, tweet):
        f = open("important_tweets.txt", "a")


        #in tweet we care about - timestamp, id, @user, followers, text
        first_line = "\n\n" + tweet.created_at.strftime("%Y/%m/%d, %H:%M:%S") + "\n"
        second_line = str(tweet.id) + "\n" 
        third_line = "@" + tweet.user.screen_name + " " + str(tweet.user.followers_count) + "\n"
        
        try:      
            fourth_line = tweet.extended_tweet["full_text"] + "\n"
        except AttributeError:
            fourth_line = tweet.text + "\n"

        # print('Wrinting to file.')    
        f.write(first_line)
        f.write(second_line)
        f.write(third_line)
        f.write(fourth_line)
        f.close()
            
        