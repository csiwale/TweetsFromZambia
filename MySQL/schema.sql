--
-- mysql_database_schema.sql
--
USE TweetsFromZambia;

CREATE TABLE IF NOT EXISTS 'json_cache' (
  'cache_id' int(10) unsigned NOT NULL AUTO_INCREMENT,
  'tweet_id' bigint(20) unsigned NOT NULL,
  'cache_date' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  'raw_tweet' text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY ('cache_id'),
  KEY 'tweet_id' (`tweet_id`),
  KEY 'cache_date' (`cache_date`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS 'tweets' (
  'tweet_id' bigint(20) unsigned NOT NULL REFERENCES json_cache(tweet_id),
  'tweet_text' varchar(160) NOT NULL,
  'created_at' datetime NOT NULL,
  'coordinates' varchar(150) NOT NULL,
  'entities' text CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  'favorite_count' int(20) DEFAULT NULL,
  'place' text CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  'retweeted' boolean NOT NULL,
  'retweet_count' int(20) NOT NULL,
  'retweeted_status' varchar(160) DEFAULT NULL,
  'source' varchar(200) NOT NULL,
  'user' text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  'user_id' bigint(20) unsigned NOT NULL,
  'screen_name' char(20) NOT NULL,	
  'name' varchar(20) DEFAULT NULL,
  'profile_image_url' varchar(200) DEFAULT NULL,
  PRIMARY KEY (`tweet_id`),
  KEY 'created_at' ('created_at'),
  KEY 'user_id' ('user_id'),
  KEY 'screen_name' ('screen_name'),
  KEY 'name' ('name'),
  FULLTEXT KEY 'tweet_text' ('tweet_text')
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS 'tweet_mentions' (
  'tweet_id' bigint(20) unsigned NOT NULL REFERENCES json_cache(tweet_id),
  'source_user_id' bigint(20) unsigned NOT NULL,
  'target_user_id' bigint(20) unsigned NOT NULL,
  KEY 'tweet_id' ('tweet_id'),
  KEY 'source' ('source_user_id'),
  KEY 'target' ('target_user_id')
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS 'tweet_tags' (
  'tweet_id' bigint(20) unsigned NOT NULL REFERENCES json_cache(tweet_id),
  'tag' varchar(100) NOT NULL,
  KEY 'tweet_id' ('tweet_id'),
  KEY 'tag' ('tag')
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS 'tweet_urls' (
  'tweet_id' bigint(20) unsigned NOT NULL REFERENCES json_cache(tweet_id),
  'url' varchar(140) NOT NULL,
  KEY 'tweet_id' ('tweet_id'),
  KEY 'url' ('url')
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS 'users' (
  'user_id' bigint(20) unsigned NOT NULL,
  'entities' text CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  'favourites_count' int(20) NOT NULL,
  'geo_enabled' boolean NOT NULL,
  'screen_name' varchar(20) NOT NULL,
  'name' varchar(20) DEFAULT NULL,
  'profile_image_url' varchar(200) DEFAULT NULL,
  'location' varchar(30) DEFAULT NULL,
  'url' varchar(200) DEFAULT NULL,
  'description' varchar(200) DEFAULT NULL,
  'created_at' datetime NOT NULL,
  'followers_count' int(10) unsigned DEFAULT NULL,
  'friends_count' int(10) unsigned DEFAULT NULL,
  'statuses_count' int(10) unsigned DEFAULT NULL,
  'time_zone' varchar(40) DEFAULT NULL,
  'last_update' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
     ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY ('user_id'),
  KEY 'user_name' ('name'),
  KEY 'last_update' ('last_update'),
  KEY 'screen_name' ('screen_name'),
  FULLTEXT KEY 'description' ('description')
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS 'tweet_places' (
	'tweet_id' bigint(20) unsigned NOT NULL REFERENCES json_cache(tweet_id),
    'full_name' varchar(60) NOT NULL,
    'place_name' varchar(20) NOT NULL,
    'bounding_box' varchar(200) NOT NULL,
    KEY 'place_name' ('place_name')
) ENGINE=MyISAM DEFAULT CHARSET=utf8;