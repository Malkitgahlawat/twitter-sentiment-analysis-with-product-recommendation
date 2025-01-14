import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from text_processing import TextProcessor
from recommendations import RecommendationEngine
from tweepy.errors import TweepyException, Forbidden

class TwitterClient:
    def __init__(self):
        try:

            self.auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)
            self.processor = TextProcessor()
            self.recommender = RecommendationEngine()
        except Exception as e:
            print("Error: Authentication Failed", e)

    def fetch_tweets(self, query, count=10):

        try:

            tweets = []
            for tweet in tweepy.Cursor(self.api.search_tweets, q=query, count=count, lang='en').items(count):
                parsed_tweet = {
                    'text': tweet.text,  # Full tweet text
                    'sentiment': self.processor.get_tweet_sentiment(tweet.text)
                }
                tweets.append(parsed_tweet)
            return tweets
        except Forbidden as e:
            print("Access Forbidden: ", e)
        except TweepyException as e:
            if 'Rate limit exceeded' in str(e):
                print("Rate limit exceeded. Try again later.")
            else:
                print("Tweepy error occurred: ", e)
        except Exception as e:
            print("Error:", str(e))
        return []



