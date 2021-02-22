

class AdvancedTweetHandler():


    def get_category(self, status, text):
        count = 0
        categories = []


        for ticker in self.tickers:
            if ticker.lower() in text:
                categories.append(ticker)
                count += 1



        if count != 1:
            # print('Multiple potential categories detected')
            # return ''
        # elif count <= 0:
            print('Detected multiple or no categories')
            return 'null'
        else:
            return categories[0]




    def is_spam(self, status):

        #extract text from tweet
        if 'extended_tweet' in status:
            text = status.extended_tweet['full_text'].lower()
        else:
            text = status.text.lower()

        #get main ticker
        ticker = self.get_category(text=text)

        #get general and ticker index
        general_index = self.tickers.index('GENERAL')

        #check for all phrases in general rules
        for phrase in self.discard_phrases[general_index]:
            if phrase in text:
                return True


        #get index of the ticker found
        if ticker != 'null':

            ticker_index = self.tickers.index(ticker)

            #check for all phrases in particular ticker's rules
            for phrase in self.discard_phrases[ticker_index]:
                if phrase in text:
                    return True


        #text passed spam check
        return False



    def is_important(self, status):
        
        importance_value = 0
        
        #extract text from tweet
        if 'extended_tweet' in status:
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
                importance_value += 1

        #check ticker's keyphrases if not null
        if ticker != 'null':
            ticker_index = self.tickers.index(ticker)

            for phrase in self.keyphrases[ticker_index]:
                if phrase in text:
                    importance_value += 1


        return importance_value >= self.importance_threshold



    def set_tickers(self, tickers):
        self.tickers = tickers

    def scan_for_tickers(self, delimiter, filename):
        tickers_count = 0

        with open(filename) as file:
            for line in file:
                if delimiter in line:
                    tickers_count += 1
        return tickers_count


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




    def __init__(self):

        discard_filename = 'tweet_discard_phrases.txt'
        keyword_filename = 'tweet_keywords.txt'
        delimiter = '___'   

        self.followers_threshold = 500
        self.importance_threshold = 4
        self.discard_phrases = []
        self.keyphrases = []
        self.tickers = []

        self.load_phrases(delimiter=delimiter, filename=discard_filename, dest_array=self.discard_phrases)
        self.load_phrases(delimiter=delimiter, filename=keyword_filename, dest_array=self.keyphrases)

        print(self.tickers)
        print(self.discard_phrases)
        print(self.keyphrases)




t = AdvancedTweetHandler()
