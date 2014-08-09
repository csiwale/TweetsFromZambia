import twitter
import json

CONSUMER_KEY = 'uz1mF8q2Ycq8hTtiq1pGukQbl'
CONSUMER_SECRET = 'kaPNxbCI0p31Xu3t2ASw80FuTnjVr9CBDB3ZnZScojxM7epKjP'
OAUTH_TOKEN = '49647130-HnVRebqlYGCUIGFVEVuw3ngJeuQD4wCoLG3SIoMbF'
OAUTH_TOKEN_SECRET = 'TBW3iQnNQqEBLyTvhDdvIvAqISn9MSAE8XsdnB2U39m8R'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
ZAMBIA_WOE_ID = 23425003

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
zambia_trends = twitter_api.trends.place(_id=ZAMBIA_WOE_ID)

print(world_trends)
print
print(zambia_trends)

