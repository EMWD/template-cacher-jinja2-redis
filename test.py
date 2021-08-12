import json
import redis

# redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# splitted_html = []
# with open('templates/template.html') as f:
#     for line in f:
#        splitted_html.append(line)

# # print(len(splitted_html))

# json_html = json.dumps(splitted_html)
# redis.set('key_word', json_html)

# result = json.loads(redis.get('key_word'))
# print(result)

from cacher import cacher

print(cacher.run())