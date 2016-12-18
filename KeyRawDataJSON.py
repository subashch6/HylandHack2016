class KeyRawDataJSON:
    def __init__(self, list_key):
        # Convert all tweets to JSON format
        self.key_json_txt = '{"key_follower_tweets":['
        for tweets in list_key:
            self.key_json_txt += '{"tweet_text": "' + tweets.tweet_text.encode('utf-8') + '", "id":' + str(
                tweets.tweet_id) + ',"retweets":' + str(
                tweets.retweets) + ',"date":"' + str(tweets.date) + '","emotion_scores":' + str(
                tweets.emotion_scores) + '},'
        self.key_json_txt = self.key_json_txt[:-1]
        self.key_json_txt += ']}'
        self.key_json_txt.replace('\n', '')

    def createJSON(self):
        f = open('raw_key_tweets.json', 'w')
        f.write(self.key_json_txt)
