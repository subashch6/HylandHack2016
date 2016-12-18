from TweetSpecificationSearch import TweetSpecificationSearch
from IndicoOriginal import IndicoOriginal
from Datamuse import Datamuse
from IndicoAllFollowerTweet import IndicoAllFollowerTweet
from IndicoKeyFollowerTweet import IndicoKeyFollowerTweet
from DataProcessing import DataProcessing
from AllRawDataJSON import AllRawDataJSON
from KeyRawDataJSON import KeyRawDataJSON
import sys

command_inputs = sys.argv
account_name = command_inputs[1]
tweet_text = command_inputs[2]

print account_name
print type(account_name)
print tweet_text
print type(tweet_text)
if account_name[0] == '@':
    account_name = account_name[1:]
# account_name = 'What_The_Phuoc'
# tweet_text = 'We get 10 free counseling sessions from OSU, I\'m about to use all 10 of them'

# IndicoOriginal
original_tweet = IndicoOriginal(account_name, tweet_text)
org_keywords = original_tweet.keywords

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

# Test IndicoKeyFollowerTweet
keyword_follower_tweet_objects = []
for tweet_obj in keyword_tweet_list:
    keyword_follower_tweet_objects.append(IndicoKeyFollowerTweet(tweet_obj))

# create aggregate data JSON
process_data = DataProcessing(original_tweet, keyword_follower_tweet_objects, all_follower_tweet_objects)
process_data.export_json()

# create raw all tweet JSON
all_raw_data = AllRawDataJSON(all_follower_tweet_objects)
all_raw_data.createJSON()

# create raw key tweet JSON
key_raw_data = KeyRawDataJSON(keyword_follower_tweet_objects)
key_raw_data.createJSON()
