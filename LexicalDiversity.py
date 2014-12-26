__author__ = 'csiwale'

import sys

# A function for computing lexical diversity
def lexical_diversity(tokens):
    return 1.0*len(set(tokens))/len(tokens)


# A function for computing the average number of words per tweet
def average_words(statuses):
    total_words = sum([ len(s.split()) for s in statuses ])
    return 1.0*total_words/len(statuses)

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

    print(lexical_diversity(words))
    print(lexical_diversity(hashtags))
    print(lexical_diversity(screen_names))
    print(lexical_diversity(source))

    print(average_words(tweet_texts))