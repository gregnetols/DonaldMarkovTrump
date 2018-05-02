import HistoricTweets


def main():

    historic_tweets = HistoricTweets.tweet_history()

    for idx, tweet in enumerate(historic_tweets):
        print(idx, tweet.id)





if __name__ == "__main__":
    main()

