class DataProcessing:
    def __init__(self, original_tweet, list_key, list_all):
        # copy original tweet values
        self.handle = original_tweet.handle
        self.tweet = original_tweet.tweet
        self.twitter_engagement = original_tweet.twitter_engagement
        self.personality_scores = original_tweet.personality_scores
        self.political_scores = original_tweet.political_scores
        self.keywords = original_tweet.keywords
        # actual processing to get - aggregate personality, political, emotional scores
        self.aggregate_personality_scores = self.aggregate_personality(list_all)
        self.aggregate_political_scores = self.aggregate_political(list_all)
        self.aggregate_emotion_scores = self.aggregate_emotion(list_key)

    def aggregate_personality(self, list_all):
        personality_scores = [0, 0, 0, 0]
        num_tweets = 0
        for ind_tweet in list_all:
            multiplying_factor = ind_tweet.retweets + 1
            num_tweets += multiplying_factor
            for i in range(0, 4):
                personality_scores[i] += ind_tweet.personality_values[i] * multiplying_factor
        for i in range(0, 4):
            personality_scores[i] /= num_tweets
        return personality_scores

    def aggregate_political(self, list_all):
        political_scores = [0, 0, 0, 0]
        num_tweets = 0
        for ind_tweet in list_all:
            multiplying_factor = ind_tweet.retweets + 1
            num_tweets += multiplying_factor
            for i in range(0, 4):
                political_scores[i] += ind_tweet.political_values[i] * multiplying_factor
        for i in range(0, 4):
            political_scores[i] /= num_tweets
        return political_scores

    def aggregate_emotion(self, list_key):
        emotion_scores = [0, 0, 0, 0, 0]
        num_tweets = 0
        for ind_tweet in list_key:
            multiplying_factor = ind_tweet.retweets + 1
            num_tweets += multiplying_factor
            for i in range(0, 5):
                emotion_scores[i] += ind_tweet.emotion_scores[i] * multiplying_factor
        for i in range(0, 5):
            emotion_scores[i] /= num_tweets
        return emotion_scores

    def export_json(self):
        keyword_str = "["
        for keyword in self.keywords:
            keyword_str += '"' + keyword + '",'
        keyword_str = keyword_str[:-1] + "]"

        org_json_txt = '{"org_tweet":['
        org_json_txt += '{"handle":"' + str(self.handle) + '","tweet": "' + self.tweet.encode(
            'utf-8') + '", "twitter_engagement":' + str(
            self.twitter_engagement) + ',"personality_scores":' + str(
            self.personality_scores) + ',"political_scores":' + str(
            self.political_scores) + ',"keywords":' + keyword_str + ',"aggregate_political_scores":' + str(
            self.aggregate_political_scores) + ',"aggregate_personality_scores":' + str(
            self.aggregate_personality_scores) + ',"aggregate_emotion_scores":' + str(
            self.aggregate_emotion_scores) + '},'
        org_json_txt = org_json_txt[:-1]
        org_json_txt += ']}'
        org_json_txt.replace('\n', '')
        f = open('aggregate_data.json', 'w')
        f.write(org_json_txt)
