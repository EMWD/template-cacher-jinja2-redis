#!/usr/bin/python3
import json
import redis
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
        with open(path) as f:
            return [line for line in f]


    def html_to_json(self, html_dict):
        return json.dumps(html_dict)


    def redis_set(self, json_html):
        self.redis.set('key_word', json_html)


    def cache_template(self, path):
        html_dict = self.scan_template(path)
        jsoned_html = self.html_to_json(html_dict)
        self._redis.set('key_word', jsoned_html)
        return None

    def get_cache(self):
        return json.loads(self._redis.get('key_word'))


cacher = Cacher()
