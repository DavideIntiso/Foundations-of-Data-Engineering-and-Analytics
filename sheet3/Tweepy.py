# OAuth2.0 Version
import tweepy
import csv

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAABLtjAEAAAAAATSEt6gf5Z%2FazcZbqr4L%2F92LXRo%3DaH6ZLVw7DB3OdM2EoVVqZv2k4OheB4GEOeBAy3RRiV1CuizbbP')


# Get tweets that contain the word Innsbruck
# -is:retweet means I don't wantretweets
query = 'Innsbruck -is:retweet'

# Name and path of the file where you want the Tweets written to
file_name = 'tweets.csv'

with open(file_name, 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(
            limit=50):
        response = client.get_liking_users(tweet.id)
        metadata = response.meta["result_count"]
        filehandle.write('%s' % tweet.id + ',' + str(metadata) + '\n')
