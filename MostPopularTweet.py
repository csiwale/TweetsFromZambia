__author__ = 'csiwale'

import sys
import json
import io

def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
    # You could also consider using the favorite_count parameter as part of
    # this heuristic, possibly using it to provide an additional boost to
    # popular tweets in a ranked formulation
    return [ status for status in statuses if status['retweet_count'] > retweet_threshold ]

def load_json(filename):
    with io.open('{0}.json'.format(filename), encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    tweets = open(sys.argv[1])
    results = load_json('JSON')
    print json.dumps(results, indent=5)
    #evaluate tweets
    #for line in tweets:
     #   try:
      #      tweet = json.loads(line)
       #     print tweet["text"]
        #except Exception as e:
         #   print e


