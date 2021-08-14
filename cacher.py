#!/usr/bin/python3
import json
from config import cfg


class Cacher():
    _redis = None

    def __init__(self) -> None:
        import redis
        self._redis = redis.StrictRedis(
            host=cfg.get('host'),
            port=cfg.get('port'),
            db=cfg.get('db')
        )

    def scan_template(self, path='templates/template.html'):
        '''
        Scanning(reading) the specified template
        '''
        with open(path) as f:
            return [line for line in f]

    def html_to_json(self, html_dict):
        '''
        Converting transferred template from html to json
        '''
        return json.dumps(html_dict)

    def redis_set(self, jsoned_html, keyword='all'):
        '''
        Set json format data to redis storage by keyword 
        '''
        self._redis.set(keyword, jsoned_html)

    def cache_template(self, path, key_word='all'):
        '''
        Performs a series of operations between class methods
        '''
        html_dict = self.scan_template(path)
        jsoned_html = self.html_to_json(html_dict)
        self.redis_set(jsoned_html, key_word)
        return None

    def get_cache(self, key_word='all'):
        '''
        Receives data from redis storage by keyword
        '''
        redis_data = self._redis.get(key_word)
        if redis_data is None:
            raise KeyError(f"Cacher error not cached data by this keyword:{key_word}")
        return redis_data

# Cahcer export
cacher = Cacher()
