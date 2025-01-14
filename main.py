from twitter_client import TwitterClient

def main():
    api = TwitterClient()
    topic = "Electric Cars"
    count = 10
    tweets = api.fetch_tweets(query=topic, count=count)

    for idx, tweet in enumerate(tweets[:5], start=1):
        print(f"{idx}. Text: {tweet['text']}")
        print(f"   Sentiment: {tweet['sentiment']}")
        print(f"   Emotions: {tweet['emotions']}")
        print(f"   Recommendation: {tweet['recommendation']}")
        print()

if __name__ == "__main__":
    main()


