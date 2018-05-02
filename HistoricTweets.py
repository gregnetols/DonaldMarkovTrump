from Tweet import Tweet


def tweet_history():
    """Processes the full history of trump tweets and puts them into tweet objects"""
    tweets = []

    row_number = 0
    for line in open('TrumpTweets.txt'):
        row_number += 1

        line = line.split(',')
        try:
            tweet = Tweet(tweet_source=line[0], tweet_text=line[1], tweet_date=line[2], tweet_id=line[6])
            tweets.append(tweet)
        except IndexError:
            print("Tweet {} was not formatted correctly".format(row_number))

    return tweets



