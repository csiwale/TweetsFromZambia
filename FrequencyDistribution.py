__author__ = 'csiwale'

import sys
from collections import Counter
from prettytable import PrettyTable

def get_words(file):
    with open(file, 'r') as f:
        words = f.readlines()
        c = Counter(words)
        print c.most_common()[:10]

if __name__ == '__main__':
    get_words(sys.argv[1])