__author__ = 'csiwale'

import json
import sys
from collections import defaultdict
import pandas as pd
import re

tweets = [];

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

def tweet_time_plot(file):
    tweets = [json.loads(line) for line in open(file)]
    print tweets[0]
    tweet_time = [tweet['created_at'].split()[3].split(':')[0] for tweet in tweets]
    time_series = pd.Series(tweet_time)
    time_series_count = time_series.value_counts()
    time_series_count.plot(kind='barh', rot=0)

def tweet_source_plot(file):
    sources = [re.match('<a (.*)>(.*)</a>', tweet['source']).group(2) for tweet in tweets]

if __name__ == '__main__':
    tweet_time_plot(sys.argv[1])

