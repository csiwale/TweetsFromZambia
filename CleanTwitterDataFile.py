__author__ = 'csiwale'

import sys
import json
import io
import re

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

    error_tweets = open('error_tweets.txt', 'a')
    clean_tweets = open('cleaned_tweets.txt', 'a')
    TwitterData0_cleaned = open('TwitterData0_Cleaned.txt', 'a')

    num = 1
    #evaluate tweets
    for line in tweets:
        num = num+1
        try:
            #print (line)
            matchobj = re.match('(.*)<a href=(.*)</a>"(.*)', line)
            #print(matchobj.group(2))
            dq_url = matchobj.group(2)
            sq_url = dq_url.replace('"', "'")
            #print(sq_url)
            line = line.replace(dq_url, sq_url)
            #tweet = json.loads(line)
            #print(tweet["text"])
            TwitterData0_cleaned.write(line)
        except Exception as e:
            #error_tweets.write(line)
            print (e, num)
