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
            
        
    def save_ticker_reads(self, tickers_values):

        for ticker in tickers_values:

            filename = 'mentions_' + ticker['name'] + '.txt'
            value = ticker['value']

            f = open(filename, 'a')
            f.write(value)
            f.close()

    def save_important_tweet(self, ticker, status): #status == tweeter object

        if ticker == 'null':
            # print('Null ticker given')
            return

        filename = 'important_' + ticker + '.txt'


        first_line = "\n\n\n" + status.created_at.strftime("%Y/%m/%d, %H:%M:%S") + "\n"
        second_line = str(status.id) + "\n" 
        third_line = "@" + status.user.screen_name + " " + str(status.user.followers_count) + "\n"




        # if 'extended_tweet' in status:
        if status.truncated:
            fourth_line = status.extended_tweet['full_text']
            
        else:
            fourth_line = status.text


        f = open(filename, 'a')

        f.write(first_line)
        f.write(second_line)
        f.write(third_line)
        f.write(fourth_line)        

        f.close()