import twitter
import json
import io
import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine

def oauth_login():
    CONSUMER_KEY = 'uz1mF8q2Ycq8hTtiq1pGukQbl'
    CONSUMER_SECRET = 'kaPNxbCI0p31Xu3t2ASw80FuTnjVr9CBDB3ZnZScojxM7epKjP'
    OAUTH_TOKEN = '49647130-HnVRebqlYGCUIGFVEVuw3ngJeuQD4wCoLG3SIoMbF'
    OAUTH_TOKEN_SECRET = 'TBW3iQnNQqEBLyTvhDdvIvAqISn9MSAE8XsdnB2U39m8R'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return twitter_api


def in_zambia(coord):
    try:
        if not (coord[0] >= 22.070259 & coord[0] <= 33.485053) & (coord[1] >= -18.141344 & coord[1] <= -7.951179):
            return False
    except BaseException:
        return False
    return True

def make_twitter_request(twitter_api_func, max_errors=100, *args, **kw):
    # A nested helper function that handles common HTTPErrors. Return an updated
    # value for wait_period if the problem is a 500 level error. Block until the
    # rate limit is reset if it's a rate limiting issue (429 error). Returns None
    # for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
        if wait_period > 7200: # Seconds
            print >> sys.stderr, 'Too many retries. Quitting.'
            raise e
        # See https://dev.twitter.com/docs/error-codes-responses for common codes
        if e.e.code == 401:
            print >> sys.stderr, 'Encountered 401 Error (Not Authorized)'
            return None
        elif e.e.code == 404:
            print >> sys.stderr, 'Encountered 404 Error (Not Found)'
            return None
        elif e.e.code == 429:
            print >> sys.stderr, 'Encountered 429 Error (Rate Limit Exceeded)'
            if sleep_when_rate_limited:
                print >> sys.stderr, "Retrying in 15 minutes...ZzZ..."
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print >> sys.stderr, '...ZzZ...Awake now and trying again.'
                return 2
            else:
                raise e # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print >> sys.stderr, 'Encountered %i Error. Retrying in %i seconds' % \
                (e.e.code, wait_period)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e
    # End of nested helper function

    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError, e:
            error_count = 0
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError, e:
            error_count += 1
            print >> sys.stderr, "URLError encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise
        except BadStatusLine, e:
            error_count += 1
            print >> sys.stderr, "BadStatusLine encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise

#save json
def save_json(filename, data):
    with io.open('{0}.json'.format(filename), 'a', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False))+'\n')

#save text
def save_text(filename, data):
    with io.open('{0}.txt'.format(filename), 'a', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False))+'\n')



if __name__ == '__main__':
    twitter_api = oauth_login()

    locations = "21.999370574951172, -18.07947349548334, 33.705703735351634, -8.224360466003397"
    q = 'Zambia' #Comma-separated list of terms

    print >> sys.stderr, 'Filtering the public timeline for track = "%s %s"' % (q,locations,)

    #Reference the self.auth parameter
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

    #See https://dev.twitter.com/docs/streaming-apis
    #stream = twitter_stream.statuses.filter(track=q)
    #stream = twitter_stream.statuses.filter(locations=locations)
    #stream = make_twitter_request(twitter_stream.statuses.filter, track=q)
    stream = make_twitter_request(twitter_stream.statuses.filter, locations=locations)
    #stream = twitter_stream.statuses.sample()

    for line in stream:
        try:
            if "zambia" in line['user']['location'].lower() or "zambia" in line['place'].lower():
                print(unicode(json.dumps(line, ensure_ascii=False)))
                save_json('TwitterData', line)
                save_text('TwitterData', line)
        except Exception:
            continue
