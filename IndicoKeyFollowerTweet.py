import indicoio

indicoio.config.api_key = 'ef7ee5da29aeb3a048309547148b8afc'


class IndicoKeyFollowerTweet:
    # creates object for single tweet from follower with keyword(s)
    def __init__(self, tweet_obj):
        self.tweet_text = tweet_obj.text
        self.tweet_id = tweet_obj.id
        self.retweets = tweet_obj.retweet_count
        self.date = str(tweet_obj.created_at)
        self.emotion_scores = self.get_emotions()

    # returns personality scores - anger, joy, fear, sadness, surprise
    def get_emotions(self):
        emotion_scores = [0, 0, 0, 0, 0]
        emotion_dict = indicoio.emotion(self.tweet_text)
        for key, value in emotion_dict.iteritems():
            if key == 'anger':
                emotion_scores[0] = value
            elif key == 'joy':
                emotion_scores[1] += value
            elif key == 'fear':
                emotion_scores[2] += value
            elif key == 'sadness':
                emotion_scores[3] += value
            elif key == 'surprise':
                emotion_scores[4] += value
        return emotion_scores
