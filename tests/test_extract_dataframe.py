import unittest
import pandas as pd
import sys, os
import pprint
from textblob import TextBlob 


sys.path.append(os.path.abspath(os.path.join("../..")))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "./data/sample_data.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
_, tweet_list = read_json(sampletweetsjsonfile)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_find_statuses_count(self):
        self.assertEqual(
            self.df.find_statuses_count()[0],tweet_list[0] ) #<provide a list of the first five status counts>
        
    def test_find_full_text(self):
        text = self.df.find_full_text()   #<provide a list of the first five full texts>
        self.assertEqual(self.df.find_full_text(), text)

    def test_find_sentiments(self):
        polarity = []
        subjectivity = []
        for t in tweet_list:
            sentiment = TextBlob(t).sentiment
            polarity.append(sentiment.polarity)
            subjectivity.append(sentiment.subjectivity)
            
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            (
                subjectivity[:6],# <provide a list of the first five sentiment values>,
                polarity[:6]# <provide a list of the first five polarity values>,
            ),
        )


    def test_find_screen_name(self):
        name =[tweet['user']['name'] for tweet in tweet_list] #<provide a list of the first five screen names>
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [tweet['user']['followers_count'] for tweet in tweet_list]#<provide a list of the first five follower counts>
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [tweet['user']['friends_count']  for tweet in tweet_list]#<provide a list of the first five friend's counts>
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        possibly_sensitive =[x['possibly_sensitive'] for x in self.tweets_list]
        self.assertEqual(self.df.is_sensitive(), 
        possibly_sensitive)


    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

