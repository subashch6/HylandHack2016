from TweetSpecificationSearch import TweetSpecificationSearch
from IndicoOriginal import IndicoOriginal
from Datamuse import Datamuse
from IndicoAllFollowerTweet import IndicoAllFollowerTweet
from IndicoKeyFollowerTweet import IndicoKeyFollowerTweet


account_name = 'OnBase'
tweet_text = 'Raffle tickets and Rock Band at the 2009 Hyland Holiday Party! #HylandLife #TBT'

# IndicoOriginal
original_tweet = IndicoOriginal(account_name, tweet_text)
org_keywords = original_tweet.keywords

# convert original tweet into json
org_json_txt = '{"org_tweet":['
org_json_txt += '{"handle":"'+str(original_tweet.handle)+'","tweet": "' + original_tweet.tweet.encode('utf-8') + '", "twitter_engagement":' + str(
    original_tweet.twitter_engagement) + ',"personality_scores":' + str(
    original_tweet.personality_scores) + ',"political_scores":' + str(original_tweet.political_scores) + ',"keywords":' + str(
    original_tweet.keywords)+'},'
org_json_txt = org_json_txt[:-1]
org_json_txt += ']}'

# Datamuse to add additional keywords
word_adder = Datamuse()
all_keywords = []
all_keywords.extend(org_keywords)
for term in org_keywords:
    # TODO change limit
    params = {'ml': term, 'max': 10}
    new_words = word_adder.words(**params)
    for temp_dicts in new_words:
        for key, value in temp_dicts.iteritems():
            if key == 'word':
                print value
                all_keywords.append(value)
print all_keywords

# TweetSpecificationSearch
follower_analysis = TweetSpecificationSearch(account_name, all_keywords)
tweet_list = follower_analysis.retrieve_tweet_objects()
keyword_tweet_list = tweet_list[0]
all_tweet_list = tweet_list[1]

# TODO set limit on number of runs here
keyword_tweet_list = keyword_tweet_list[:10]
all_tweet_list = all_tweet_list[:10]

# Test IndicoAllFollowerTweet
all_follower_tweet_objects = []
for tweet_obj in all_tweet_list:
    all_follower_tweet_objects.append(IndicoAllFollowerTweet(tweet_obj))

# Convert all tweets to JSON format
all_json_txt = '{"all_follower_tweets":['
for tweets in all_follower_tweet_objects:
    all_json_txt += '{"tweet_text": "' + tweets.tweet_text.encode('utf-8') + '", "id":'+str(tweets.tweet_id)+',"retweets":'+str(tweets.retweets)+',"date":"'+str(tweets.date)+'","personality_values":'+str(tweets.personality_values)+',"political_values":'+str(tweets.political_values)+'},'
all_json_txt = all_json_txt[:-1]
all_json_txt += ']}'
print all_json_txt

# Test IndicoKeyFollowerTweet
keyword_follower_tweet_objects = []
for tweet_obj in keyword_tweet_list:
    keyword_follower_tweet_objects.append(IndicoKeyFollowerTweet(tweet_obj))

# Convert key tweets to JSON format
key_json_txt = '{"key_follower_tweets":['
for tweets in keyword_follower_tweet_objects:
    key_json_txt += '{"tweet_text": "' + tweets.tweet_text.encode('utf-8') + '", "id":' + str(
        tweets.tweet_id) + ',"retweets":' + str(
        tweets.retweets) + ',"date":"' + str(tweets.date) + '","emotion_scores":' + str(
        tweets.emotion_scores)+'},'
key_json_txt = key_json_txt[:-1]
key_json_txt += ']}'
print key_json_txt
print org_json_txt
