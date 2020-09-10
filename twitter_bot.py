import nba_api
import tweepy 

CONSUMER_KEY = 'W3YtYRltVIpTDhFT2JkVp5Dso'
CONSUMER_SECRET = '5Lld9LmTm66EAb9vQyYuoOpMLt8IzR8ZfFP8V6lRPKk7lpaS5y'
ACCESS_KEY = '1304156695635976194-oqLs8Xa6DWZf9ziMXiYHsgkHq7SvQ5'
ACCESS_SECRET = '7eBxgyxwrYbE2bWE08QJojzD0F6yQMRamjDED6ttLKmRH'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth .set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print(tweet.text)

# user = api.get_user('nateluu28')
# print(user.screen_name)
# print(user.followers_count)

# for friend in user.friends():
#   print(friend.screen_name)


mentions = api.mentions_timeline()


print(mentions[0].text)

