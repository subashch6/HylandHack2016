import tweepy

class TweetSpecificationSearch:
    def __init__(self, account_name, keywords):
        # set twitter credentials
        consumer_key = "c9R6Tn26B0nr55j4OpdxIvvh1"
        consumer_secret = "1V4gOqr1LUPO4kKkiGtrRlPn26486IEHnl6jEbTDBvAZrOsATO"
        access_token = "798334110448160768-evbz3r5XF9mCI8VUmdSlYDsfkPhexyP"
        access_token_secret = "TBOOnKZROrMX61093Q0thMJ5g7Fztv9inVJGYuDz21F3D"

        # enter credentials
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

        # set account name and keywords
        self.account_name = account_name
        self.keywords = keywords

    def change_keywords(self, keywords):
        self.keywords = keywords

    def retrieve_tweet_objects(self):
        key_tweet_objects = []
        all_tweet_objects = []

        # get followers of account
        followers_list = self.api.followers_ids(self.account_name)
        f_counter = 0

        # TODO change counter values
        while len(key_tweet_objects) < 100 and f_counter < 50:
            cur_follower = self.api.get_user(followers_list[f_counter])
            f_counter += 1
            cur_name = cur_follower.screen_name
            print cur_name
            try:
                tweet_list = self.api.user_timeline(screen_name=cur_name, count=50)
                for tweet in tweet_list:
                    unfiltered_tweet = tweet.text
                    # tweet must not be retweet, response, or have a link
                    filter_tweet = unfiltered_tweet.replace('"', ' ').lower().replace('\n',' ')
                    tweet.text = filter_tweet
                    if filter_tweet[:2] != 'rt' and filter_tweet[:1] != '@' and \
                            'http' not in filter_tweet:
                        # print filter_tweet
                        all_tweet_objects.append(tweet)
                        # keyword tweet must contain keyword
                        if any(keyword in filter_tweet for keyword in self.keywords):
                            key_tweet_objects.append(tweet)
            except tweepy.TweepError:
                print ':('
        # form list of both lists
        comb_lists = [key_tweet_objects, all_tweet_objects]
        return comb_lists

# # just for testing 8===D
# keywords = ['hi', 'fuck', 'shit']
# test = TweetSpecificationSearch('ikezawa_', keywords)
# both_lists = test.retrieve_tweet_objects()
# key_list = both_lists[0]
# all_list = both_lists[1]
#
# key_text = []
# all_text = []
# for tweet_obj in key_list:
#     key_text.append(tweet_obj.text)
# for text in key_text:
#     print text
