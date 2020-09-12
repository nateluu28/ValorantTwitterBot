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
# to do print the bios and link to agent in a reply
for mention in mentions:
  print(mention.text)
  for agent in agents:
    if agent in mention.text:
      print(agent + 'found')
      print(mention.id)
      # api.update_status("my update", in_reply_to_status_id = mention.id)
      api.update_status("@" + mention.user.screen_name + " " + agent + " is the best!", 1304172263806124033)


# to do
# make it into a function
# retweet every 24hours? or through a mention hashtag

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#   print(tweet.id)
#   try:
#     api.retweet(tweet.id)
#   except tweepy.TweepError as e:
#     print(e)