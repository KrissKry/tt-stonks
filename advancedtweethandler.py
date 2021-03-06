

class AdvancedTweetHandler():


    def get_category(self, text=None, status=None):
        count = 0
        categories = []

        if status == None and text == None:
            return 'null'


        if status != None:
            try:        
                if status.truncated:
                    text = status.extended_tweet['full_text']
                else:
                    text = status.text
            except AttributeError:
                print('Status is kinda weird idk')
                return


        for ticker in self.tickers:
            if ticker.lower() in text.lower():
                categories.append(ticker)
                count += 1



        if count > 1:
            # print('Multiple potential categories detected')
            return 'GENERAL'
        elif count <= 0:
            # print('Detected multiple or no categories')
            return 'null'
        else:
            return categories[0]




    def is_spam(self, status):

        # extract text from tweet
        if status.truncated:
            text = status.extended_tweet['full_text'].lower()
        else:
            text = status.text.lower()

        #get main ticker
        ticker = self.get_category(text=text)

        if self.scan_for_spam(ticker, text):
            return True

        if self.scan_for_spam('GENERAL', text):
            return True

        #text passed spam check
        return False


    def scan_for_spam(self, ticker, text):

        try:
            ticker_index = self.tickers.index(ticker)
        except ValueError:
            return False

        for phrase in self.discard_phrases[ticker_index]:
            if phrase.lower() in text.lower():
                print('Spam filtered with', phrase)
                return True

        return False


    def evaluate_importance(self, status):
        
        importance_value = 0
        
        #extract text from tweet
        if status.truncated:
            text = status.extended_tweet['full_text'].lower()
        else:
            text = status.text.lower()


        followers_count = status.user.followers_count

        #get first suitable ticker for the tweet
        ticker = self.get_category(text=text)

        #check followers count
        if followers_count > 10 * self.followers_threshold:

            importance_value += 2

        elif followers_count >= self.followers_threshold:

            importance_value += 1


        #check general keyphrases
        general_index = self.tickers.index('GENERAL')

        for phrase in self.keyphrases[general_index]:
            if phrase in text:
                # print('found phrase', phrase)
                importance_value += 1

        #check ticker's keyphrases if not null
        if ticker != 'null':
            ticker_index = self.tickers.index(ticker)

            for phrase in self.keyphrases[ticker_index]:
                if phrase in text:
                    importance_value += 1


        return importance_value




    def scan_for_tickers(self, delimiter, filename):
        tickers_count = 0

        with open(filename) as file:
            for line in file:
                if delimiter in line:
                    tickers_count += 1
        return tickers_count


    def should_be_analyzed(self, status):

        return status.lang == 'en' and status.user.followers_count >= 0.5 * self.followers_threshold
        # if status.lang == 'en':# and status.user.followers_count >= self.followers_threshold:
            # return True
        # return False


    def load_phrases(self, delimiter, filename, dest_array):

        read_phrases = []
        with open(filename) as file:

            for line in file:   

                #if found '___' in line
                if delimiter in line:
                    
                    #save a copy of all phrases read for previous ticker
                    dest_array.append(list(read_phrases))
                    read_phrases.clear()


                    #get ticker string
                    ticker = line[len(delimiter) : line.index(delimiter, len(delimiter) ) ]

                    #save ticker
                    if ticker not in self.tickers:
                        self.tickers.append(ticker)


                #regular line found with keywords and keyphrases
                else:
                    for phrase in line.strip().split(', '):
                        read_phrases.append(phrase)

        #remove first list with nothing in it
        dest_array.pop(0)

        #add phrases for last ticker
        dest_array.append(list(read_phrases))


    def get_importance_threshold(self):
        return self.importance_threshold


    def __init__(self):

        discard_filename = 'config/tweet_discard_phrases.txt'
        keyword_filename = 'config/tweet_keywords.txt'
        delimiter = '___'   

        self.followers_threshold = 500
        self.importance_threshold = 3
        self.discard_phrases = []
        self.keyphrases = []
        self.tickers = []

        self.load_phrases(delimiter=delimiter, filename=discard_filename, dest_array=self.discard_phrases)
        self.load_phrases(delimiter=delimiter, filename=keyword_filename, dest_array=self.keyphrases)

        print(self.tickers)
        print(self.discard_phrases)
        print(self.keyphrases)




# t = AdvancedTweetHandler()
# t.is_spam()