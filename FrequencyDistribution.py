__author__ = 'csiwale'

import sys
from collections import Counter
from prettytable import PrettyTable


if __name__ == '__main__':
    words = open(sys.argv[1])
    hashtags = open(sys.argv[2])
    tweet_texts = open(sys.argv[3])
    screen_names = open((sys.argv[4]))
    source = open((sys.argv[5]))

    words = words.readlines()
    hashtags = hashtags.readlines()
    tweet_texts = tweet_texts.readlines()
    screen_names = screen_names.readlines()
    source = source.readlines()

    #c = Counter(words)
    #print (c.most_common()[:10])
    for label, data in (('Word', words), ('Word', words), ('Hashtag', hashtags), ('Tweet Text', tweet_texts), ('Screen Name', screen_names), ('Source', source)):
        pt = PrettyTable(field_names=[label, 'Count'])
        c = Counter(data)
        [pt.add_row(kv) for kv in c.most_common()[:10]]
        pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
        print (pt)