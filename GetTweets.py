__author__ = 'csiwale'

import sys
import json

if __name__ == '__main__':
    with open('Tweets.txt', 'w') as outfile:
        tweets = open(sys.argv[1])
        #evaluate tweets
        for line in tweets:
            line = line.strip()
            #line = line.replace("'",'"')

            try:
                tweet = dict(line)
                #print tweet.keys()
                outfile.write(tweet['text'])
                #print(json.dumps(line))
            except Exception as e:
                print(e, sys.exc_info()[0])