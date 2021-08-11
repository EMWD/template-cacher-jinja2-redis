import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

data = [
    {'type':'big', 'url':'....'},
    {'type':'big', 'url':'....'},
    {'type':'big', 'url':'....'},
]

# Convert python dict to JSON str and save to Redis
json_data = json.dumps(data)
r.set('key_word', json_data)

# Read saved JSON str from Redis and unpack into python dict
unpacked_images = json.loads(r.get('key_word'))
# data == unpacked_images

print(data)