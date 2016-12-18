import requests

class Datamuse():
    def __init__(self):
        self.api_root = 'https://api.datamuse.com'
        self.word_params = {
            'ml',
            'sl',
            'sp',
            'rel_jja',
            'rel_jjb',
            'rel_syn',
            'rel_ant',
            'rel_spc',
            'rel_gen',
            'rel_com',
            'rel_par',
            'rel_bga',
            'rel_bgb',
            'rel_rhy',
            'rel_nry',
            'rel_hom',
            'rel_cns',
            'v',
            'topics',
            'lc',
            'rc',
            'max'
        }
        self.suggest_params = {
            's',
            'max',
            'v'
        }

    def get_resource(self, endpoint, **kwargs):
        url = self.api_root + endpoint
        response = requests.get(url, params=kwargs)
        data = response.json()
        return data

    def words(self, **kwargs):
        words = '/words'
        return self.get_resource(words, **kwargs)

    def suggest(self, **kwargs):
        sug = '/sug'
        return self.get_resource(sug, **kwargs)

# test_case = Datamuse()
# params = {'ml': 'suicide', 'max': 20}
# print test_case.words(**params)
