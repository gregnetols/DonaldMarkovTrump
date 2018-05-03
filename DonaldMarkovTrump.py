import HistoricTweets
from MarkovNode import MarkovProcess

def main():

    historic_tweets = HistoricTweets.tweet_history()

    for idx, tweet in enumerate(historic_tweets):
        #print(idx, tweet.id)
        pass
    markov_chain = MarkovProcess()

    for tweet in historic_tweets:
        split_tweet = tweet.text.split()
        for idx, word in enumerate(split_tweet):
            if idx == 0:
                pass
            elif idx == len(split_tweet):
                markov_chain.add_transition(word, '')
            else:
                markov_chain.add_transition(split_tweet[idx-1], word)


if __name__ == "__main__":
    main()

  

