class AllRawDataJSON:
    def __init__(self, list_all):
        # Convert all tweets to JSON format
        self.all_json_txt = '{"all_follower_tweets":['
        for tweets in list_all:
            self.all_json_txt += '{"tweet_text": "' + tweets.tweet_text.encode('utf-8') + '", "id":' + str(
                tweets.tweet_id) + ',"retweets":' + str(tweets.retweets) + ',"date":"' + str(
                tweets.date) + '","personality_values":' + str(
                tweets.personality_values) + ',"political_values":' + str(tweets.political_values) + '},'
        self.all_json_txt = self.all_json_txt[:-1]
        self.all_json_txt += ']}'
        self.all_json_txt.replace('\n', '')

    def createJSON(self):
        f = open('raw_all_tweets.json', 'w')
        f.write(self.all_json_txt)
