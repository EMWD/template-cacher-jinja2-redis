#!/usr/bin/python3
import json
import redis


class Cacher():
    # def __init__(self):
    #     self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    # def init_redis(self):
    #     pass

    def scan_template(self, path='templates/template.html'):
        with open(path) as f:
            return [line for line in f]

    def html_to_json(self, html_dict):
        return json.dumps(html_dict)

    def redis_set(self, json_html):
        self.redis.set('key_word', json_html)

    def redis_get(self):
        json.loads(self.redis.get('key_word'))

    def run(self):
        html_dict = self.scan_template()
        jsoned_html = self.html_to_json(html_dict)
        
        import redis
        redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        redis.set('key_word', jsoned_html)

        return json.loads(redis.get('key_word'))

cacher = Cacher()