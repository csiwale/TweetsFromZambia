__author__ = 'CSiwale'

import sys
import json
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'kansenshi04',
    'database': 'TweetsFromZambia',
    'raise_on_warnings': True
}

def save_mysql(tweet_id, raw_tweet):
    query = "INSERT INTO json_cache(tweet_id, raw_tweet) VALUES(%s, %s)"
    args = (tweet_id, json.dumps(raw_tweet))
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(query, args)
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
            #query = "INSERT INTO tweets(tweet_id, tweet_text,  created_at, coordinates, entities, favourite_count," \
            #        "place, retweeted, retweet_count, retweet_status, source, user, user_id, screen_name, name, profile_url) " \
            #        "VALUES(%(tweet_id)s, %(tweet_text)s, %(created_at)s, %(coordinates)s, %(entities)s, %(favourite_count)s, " \
            #        "%(place)s, %(retweeted)s, %(retweet_count)s, %(retweet_status)s, %(source)s, %(user)s, %(user_id)s, %(screen_name)s, %(name)s, %(profile_url)s)"

            query = "INSERT INTO tweets(tweet_id, tweet_text, created_at, coordinates, retweeted, retweet_count, source, user_id) " \
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

            try:
                #args = {
                #   'tweet_id': raw_tweet['id'],
                #    'tweet_text': raw_tweet['text'],
                #    'created_at': raw_tweet['created_at'],
                #    'coordinates': json.dumps(raw_tweet['coordinates']),
                #    'entities': json.dumps(raw_tweet['entities']),
                #    'favourite_count': raw_tweet['favourite_count'],
                #    'place': json.dumps(raw_tweet['place']),
                #    'retweeted': raw_tweet['retweeted'],
                #    'retweet_count': raw_tweet['retweet_count'],
                #    'retweet_status': raw_tweet['retweet_status'],
                #    'source': raw_tweet['source'],
                #    'user': json.dumps(raw_tweet['user']),
                #    'user_id': raw_tweet['user']['id'],
                #    'screen_name': raw_tweet['screen_name'],
                #    'name': raw_tweet['name'],
                #    'profile_url': raw_tweet['profile_url']
                #}

                args = (raw_tweet['id'], raw_tweet['text'].encode('UTF-8'), raw_tweet['created_at'], json.dumps(raw_tweet['coordinates']), raw_tweet['retweeted'], raw_tweet['retweet_count'], raw_tweet['source'], raw_tweet['user']['id'])

            except KeyError as err:
                print (err)

            cursor.execute(query, args)
            #print query
            #print raw_tweet['text']
            cnx.commit()
        else:
            print('last insert id not found')
            cnx.rollback()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()



if __name__ == '__main__':
    tweets = open(sys.argv[1])
    for line in tweets:
        #line = line.decode('ascii')
        tweet = json.loads(line)
        save_mysql(tweet['id'], tweet)
