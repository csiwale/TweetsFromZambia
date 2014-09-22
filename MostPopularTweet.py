__author__ = 'csiwale'

import sys
import json

def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
    # You could also consider using the favorite_count parameter as part of
    # this heuristic, possibly using it to provide an additional boost to
    # popular tweets in a ranked formulation
    return [ status for status in statuses if status['retweet_count'] > retweet_threshold ]

if __name__ == '__main__':
    tweets = open(sys.argv[0])

    #evaluate tweets
    for line in tweets:
        tweet = json.loads(line)

