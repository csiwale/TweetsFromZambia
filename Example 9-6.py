import io
import json
import twitter
import sys

def save_json(filename, data):
    with io.open('{0}.json'.format(filename), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

def load_json(filename):
    with io.open('{0}.json'.format(filename), encoding='utf-8') as f:
        return f.read()

CONSUMER_KEY = 'uz1mF8q2Ycq8hTtiq1pGukQbl'
CONSUMER_SECRET = 'kaPNxbCI0p31Xu3t2ASw80FuTnjVr9CBDB3ZnZScojxM7epKjP'
OAUTH_TOKEN = '49647130-HnVRebqlYGCUIGFVEVuw3ngJeuQD4wCoLG3SIoMbF'
OAUTH_TOKEN_SECRET = 'TBW3iQnNQqEBLyTvhDdvIvAqISn9MSAE8XsdnB2U39m8R'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
# Sample usage
q = 'Zambia'

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
results = stream = twitter_stream.statuses.filter(track=q)
save_json(q, results)
results = load_json(q)
print(json.dumps(results, indent=1))
