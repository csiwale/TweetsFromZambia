__author__ = 'csiwale'

import sys
import json
from prettytable import PrettyTable

if __name__ == '__main__':
    tweets = open(sys.argv[1])
    statuses = []
    try:
        for line in tweets:
            line = json.loads(line)
            statuses.append(line)
    except Exception as e:
        print(e)

    #print(statuses)

    try:
        retweets = [
                    # Store out a tuple of these three values ...
                    (status['retweet_count'],
                     status['retweeted_status']['user']['screen_name'],
                     status['text'])

                    # ... for each tweet ...
                    for status in statuses
                        # ... so long as the tweet meets this condition.
                        if status.has_key('retweeted_status')
                   ]
    except Exception as e:
        print(e)

    try:
        # Slice off the first 5 from the sorted results and display each item in the tuple
        pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
        [ pt.add_row(row) for row in sorted(retweets, reverse=True)[:5] ]
        pt.max_width['Text'] = 50
        pt.align= 'l'
        print (pt)
    except Exception as e:
        print(e)