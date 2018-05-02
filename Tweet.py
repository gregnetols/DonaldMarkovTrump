class Tweet(object):

    def __init__(self, tweet_source, tweet_text, tweet_date, tweet_id):
        self.source = tweet_source
        self.text = tweet_text
        self.date = tweet_date
        self.id = tweet_id