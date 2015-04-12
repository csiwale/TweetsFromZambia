# IPython log file


import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\CSiwale\\Documents\\GitHub\\TweetsFromZambia'])
import json
tweets = [json.loads(line) for line in open('TwitterData3.txt')]
tweets[0]
import numpy as np
import re
source = [re.match('<a (.*)>(.*)</a>', tweet['source']).group(2) for tweet in tweets]
source[:10]
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
In [
import pandas as pd
frame = DataFrame(tweets)
from pandas import DataFrame, Series
frame = DataFrame(tweets)
frame['source'] = sources
frame['source'] = source
frame['source'][:10]
source_counts = frame['source'].value_counts()
source_counts
source_counts.plot(kind='barh', rot=0)
tweets[0]['created_at'].split()
tweets[0]['created_at'].split()[3].split()
tweets[0]['created_at'].split()[3].split()[0]
tweets[0]['created_at'].split()[3].split(':')[0]
time = [tweet['created_at'].split()[3].split(':')[0] for tweet in tweets]
time[:10]
time_series = Series(time)
time_series.value_counts()
time_series.plot(kind='barh', rot=0)
time_series_count = time_series.value_counts()
time_series_count.plot(kind='barh', rot=0)
place_name = [tweet['place']['name'] for tweet in tweets]
frame['place_name'] = place_name
place_name_counts = frame['place_name'].value_counts()
place_name_counts
time_series_count.plot()
frame['time'] = time
frame.groupby('time').id.count()
count_tweet_hr = frame.pivot_table('id', rows='time', cols='', aggfunc=count)
count_tweet_hr = frame.pivot_table('id', rows='time', cols='', aggfunc=sum)
frame.groupby('time')
frame.groupby('time').count('id')
frame.groupby('time').count('id').plot()
frame['id'].groupby('time').count('id').plot()
frame['time'].groupby('time').count('id').plot()
frame[['id','text', 'source', 'time']].groupby('time').count('id').plot()
get_ipython().magic(u'pinfo source')
source
get_ipython().magic(u'magic')
get_ipython().magic(u'quickref')
get_ipython().magic(u'gui')
get_ipython().magic(u'startlog')
get_ipython().magic(u'logstart')
