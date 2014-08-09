import twitter
import json
import sys
import oauth2

CONSUMER_KEY = 'uz1mF8q2Ycq8hTtiq1pGukQbl'
CONSUMER_SECRET = 'kaPNxbCI0p31Xu3t2ASw80FuTnjVr9CBDB3ZnZScojxM7epKjP'
OAUTH_TOKEN = '49647130-HnVRebqlYGCUIGFVEVuw3ngJeuQD4wCoLG3SIoMbF'
OAUTH_TOKEN_SECRET = 'TBW3iQnNQqEBLyTvhDdvIvAqISn9MSAE8XsdnB2U39m8R'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = 'Zambia' #Comma-separated list of terms
locations = "-18.141344,22.070259,-7.951179,33.485053"

print ('Filtering the public timeline for track="%s"' % (q,), file=sys.stderr)

#Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

#See https://dev.twitter.com/docs/streaming-apis
#stream = twitter_stream.statuses.filter(track=q)
#stream = twitter_stream.statuses.filter(locations=locations)
stream = twitter_stream.statuses.sample()

for tweet in stream:
    try:
        if "zambia" in tweet['user']['location'].lower():
            print(tweet.strip())
    except KeyError as e:
        continue
# Save to a database in a particular collection


