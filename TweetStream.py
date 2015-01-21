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
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#save text
def save_text(filename, data):
    with io.open('{0}.txt'.format(filename), 'a', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False))+'\n')



if __name__ == '__main__':
    twitter_api = oauth_login()

    zambia_bbox = "21.999370574951172, -18.07947349548334, 33.705703735351634, -8.224360466003397"

    provinces_bbox = "21.999370000005, -16.257279999990715, 23.051999999996042, -14.028600000005099," \
                     "23.47894999998971, -14.047460000001593, 24.693070000008447, -12.50046999999904," \
                     "27.50328000000445, -12.434640000006766, 28.063380000006873, -12.221380000002682," \
                     "28.624949999997625, -10.280039999997825, 29.95264999999199, -9.116769999993267," \
                     "29.802120000007562, -11.479179999994813, 30.722119999991264, -10.655249999996158" \
                     "32.15623999998206, -14.316879999998491, 33.209009999991395, -13.774929999999586," \
                     "27.15942000001087, -15.323470000002999, 28.952250000002095, -14.30633000000671," \
                     "29.27329000001191, -15.747650000004796, 30.416969999991124, -14.966679999997723," \
                     "26.69096000000718, -17.493680000014137, 27.6304999999993, -16.138299999991432"

    print >> sys.stderr, 'Filtering the public timeline by bounding box "%s"' % (zambia_bbox,)

    #Reference the self.auth parameter
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

    #See https://dev.twitter.com/docs/streaming-apis
    #stream = twitter_stream.statuses.filter(locations=locations)
    #stream = make_twitter_request(twitter_stream.statuses.filter, track=q)
    stream = make_twitter_request(twitter_stream.statuses.filter, locations=zambia_bbox)
    #stream = twitter_stream.statuses.sample()

    for line in stream:
        try:
            if "zambia" in line['user']['location'].lower() \
                    or "zambia" in line['place'].lower()\
                    or "zambia" in line['user']['location']\
                    or line['place']['country_code'] == 'ZM':
                print(unicode(json.dumps(line, ensure_ascii=False)))
                save_json('TwitterData2', line)
                save_text('TwitterData2', line)
        except Exception:
            continue
