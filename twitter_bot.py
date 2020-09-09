import tweepy 
print("this is my twitter bot")

CONSUMER_KEY = 'vqM0O5UcbC3eJI0wlexh82pil'
CONSUMER_SECRET = 'OHQnLJpbQcTXKFLWKL0c2D5f4SenG1QKtWEBu8OBl9NDOsjC9w'
ACCESS_KEY = '2282942114-95OWA1n07rzLu7KqupRecYmuyTAVICidoVhydmz'
ACCESS_SECRET = 'xKacDrQzVidoLfaMHCunj0mMzVGxnGr8izsKzOcNtX9iN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth .set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

