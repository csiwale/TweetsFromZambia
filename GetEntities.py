__author__ = 'csiwale'

import sys
import json
import io
import re

def load_json(filename):
    with io.open('{0}.json'.format(filename), encoding='utf-8') as f:
        return f.read()

def save_words(tweets):
    for line in tweets:
        #line = line.decode('ascii')
        tweet = json.loads(line)
        with open('words.txt', 'a') as words:
            try:
                for w in tweet['text'].split():
                    #w = w.encode('ascii')
                    w.rstrip(':;?,.!^-"@')
                    w.replace('\n', "")
                    words.write(w+'\n')
            except Exception as e:
                print (e)

def save_texts(tweets):
    for line in tweets:
        #line = line.decode('ascii')
        tweet = json.loads(line)
        with open('tweet_texts.txt', 'a') as tweet_texts:
            try:
                tweet_texts.write(tweet['text'] + '\n')
            except Exception as e:
                print (e)

def save_screen_names(tweets):
    for line in tweets:
        #line = line.decode('ascii')
        tweet = json.loads(line)
        with open('screen_names.txt', 'a') as screen_names:
            try:
                screen_names.write(tweet['entities']['user_mentions'][0]['screen_name'] + '\n')
            except Exception as e:
                print (e)

def save_source(tweets):
    num = 1
    for line in tweets:
        num += 1
        #line = line.decode('ascii')
        tweet = json.loads(line)
        with open('source.txt', 'a') as source:
            try:
                matchobj = re.match('<a (.*)>(.*)</a>', tweet['source'])
                print(matchobj.group(2), num)
                source.write(matchobj.group(2) + '\n')
            except Exception as e:
                print (e)

def save_hastags(tweets):
    for line in tweets:
        #line = line.decode('ascii')
        tweet = json.loads(line)
        with open('hashtags.txt', 'a') as hashtags:
            try:
                hashtags.write(tweet['entities']['hashtags'][0]['text'] + '\n')
            except Exception as e:
                print (e)

if __name__ == '__main__':
    tweets = open(sys.argv[1])
    save_words(tweets)
    #save_hastags(tweets)
    #save_screen_names(tweets)
    #save_texts(tweets)
    #save_source(tweets)

