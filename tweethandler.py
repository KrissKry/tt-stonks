import re

class TweetHandler():

    # tweet is still a status object from tweepy listener
    def check_if_important(self, tweet):
        
        # print('checking if important...')
        important_scale = 0

        # satisfies follower count
        if tweet.user.followers_count >= self.followers_threshold:
            important_scale += 1



        split_text = self.text_to_array(tweet.text)

        # satisfies important words
        for word in self.important_words:
            if self.contains_word(word, split_text):   
                important_scale += 1


        # if importance calculated is high enough
        if important_scale >= self.importance_threshold:
            # print('it is')
            return True

        # print('its not')
        return False


    def contains_word(self, word, string):
        if word in string:
            return True

        return False


    def contains_spam(self, text):

        # split_text = self.text_to_array(text)
        text = text.lower()

        for phrase in self.discard_phrases:
            if phrase in text:
                return True

        return False



    def text_to_array(self, text):

        split_text = re.split( ' |\t|\n|\r| ,|\ |\.|;|\:|\!|\?|\"\+', text)
        for x in split_text:
            x.lower()

        return split_text



    def __init__(self):
        print('Tweet Handler init innit me boy')
        self.followers_threshold = 500
        self.importance_threshold = 3
        self.important_words = ['future', 'speech', 'capitalization', 'potential', 'support','report','fundamentals', 'develops', 
                                'record','today','elon','musk', 'elonmusk','dip', 'prediction', 'bull', 'bullish', 'adoption','payment', 
                                'moon', 'buy', 'sell', 'stellar', 'boost', 'ceiling', 'roof']

        self.discard_phrases = ['freedom for', 'giving $40', 'selloff incoming', 'giveaway', 'giving away', 'follow me', 'unconfirmed reports', 'for free']
