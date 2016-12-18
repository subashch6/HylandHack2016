import indicoio
import simplejson as json

indicoio.config.api_key = 'ef7ee5da29aeb3a048309547148b8afc'


class IndicoAllFollowerTweet:
    # creates object for single tweet from any follower
    def __init__(self, tweet_obj):
        self.tweet_text = tweet_obj.text
        self.tweet_id = tweet_obj.id
        self.retweets = tweet_obj.retweet_count
        self.date = str(tweet_obj.created_at)
        self.personality_values = self.get_personality()
        self.political_values = self.get_political()

    # returns personality scores - extraversion, openness, agreeableness, conscientiousness
    def get_personality(self):
        personality_scores = [0, 0, 0, 0]
        personality_dict = indicoio.personality(self.tweet_text)
        for key, value in personality_dict.iteritems():
            if key == 'extraversion':
                personality_scores[0] += value
            elif key == 'openness':
                personality_scores[1] += value
            elif key == 'agreeableness':
                personality_scores[2] += value
            elif key == 'conscientiousness':
                personality_scores[3] += value
        return personality_scores

    # return political scores - libertarian, green, liberal, conservative
    def get_political(self):
        political_scores = [0, 0, 0, 0]
        political_dict = indicoio.political(self.tweet_text)
        for key, value in political_dict.iteritems():
            if key == 'Libertarian':
                political_scores[0] += value
            elif key == 'Green':
                political_scores[1] += value
            elif key == 'Liberal':
                political_scores[2] += value
            elif key == 'Conservative':
                political_scores[3] += value
        return political_scores
