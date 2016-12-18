import indicoio

indicoio.config.api_key = 'ef7ee5da29aeb3a048309547148b8afc'


class IndicoOriginal:
    # sets values for the original user tweet
    def __init__(self, handle, tweet):
        self.handle = handle
        self.tweet = tweet
        self.twitter_engagement = indicoio.twitter_engagement(tweet)
        self.personality_scores = self.get_personality()
        self.political_scores = self.get_political_scores()
        self.keywords = self.generate_keywords()
        for x in range(0, len(self.keywords)):
            self.keywords[x]=self.keywords[x].encode('utf-8')


    def generate_keywords(self):
        # get keywords
        keywords_dict = indicoio.keywords(self.tweet)
        all_else_dict = indicoio.analyze_text(self.tweet, apis=['places', 'people', 'organizations'])
        # store identified keywords
        keywords = []
        for key, value in keywords_dict.iteritems():
            if value > 0.2:
                keywords.append(key)
        for key, value in all_else_dict.iteritems():
            for list_item in value:
                for key_in, value_in in list_item.iteritems():
                    if key_in == 'text':
                        keywords.append(value_in)
        return keywords

    # returns personality scores - extraversion, openness, agreeableness, conscientiousness
    def get_personality(self):
        personality_scores = [0, 0, 0, 0]
        personality_dict = indicoio.personality(self.tweet)
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
    def get_political_scores(self):
        political_dict = indicoio.political(self.tweet)
        political_scores = [0, 0, 0, 0]
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
