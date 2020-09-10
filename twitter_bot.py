import tweepy
import json

CONSUMER_KEY = 'W3YtYRltVIpTDhFT2JkVp5Dso'
CONSUMER_SECRET = '5Lld9LmTm66EAb9vQyYuoOpMLt8IzR8ZfFP8V6lRPKk7lpaS5y'
ACCESS_KEY = '1304156695635976194-8Tg6H5NwZfUjD94fXm9Kj6xAs3quWP'
ACCESS_SECRET = 'tZF2HFscrDGoyZxQCUgNwBpkN7hXUQtAIWuNqn06rIuJN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth .set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

f = open('agents.json')
data = json.load(f)

for i in data['agents']:
  print(i['name'])



agents = [
  'jett',
  'raze',
  'breach',
  'omen',
  'brimstone',
  'viper',
  'phoenix',
  'killjoy',
  'reyna',
  'sage',
  'cypher'
]


mentions = api.mentions_timeline()

for mention in mentions:
  print(mention.text)
  for agent in agents:
    if agent in mention.text:
      print(agent + 'found')


# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#   print(tweet.id)
#   try:
#     api.retweet(tweet.id)
#   except tweepy.TweepError as e:
#     print(e)