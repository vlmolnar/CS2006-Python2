import unittest
import pandas as pd
import re

from code import refine as rf

class RefineTest(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv("/cs/home/js321/Documents/CS2006/python/P2/data/dummy.csv")

    # test that all rows with nan are removed - where the majority are not nan
    # The check for less than half the column is null works as if it didn't there
    # would not be any data
    # EXAMINE THE DATASET
    # EXAMINE THE DATASET
    def test_drop_nan(self):
        first_len = len(self.df)
        df = rf.removeNAN(self.df)
        self.assertFalse(first_len == len(df))

    # test that languages that are null are mapped to english
    # - reasoning for this in report
    def test_lang_nan_replace(self):
        #a null value present
        self.assertTrue(self.df["user_lang"].isnull().any())
        df = rf.langCheck(self.df)
        # nulls replaced with en
        self.assertFalse(df["user_lang"].isnull().any())

    # test that usernames are legal - alphanumeric and less than 10 chars
    def test_username_legal(self):
        length = len(self.df)
        print(self.df["from_user"])
        df = rf.fromUserCheck(self.df)
        self.assertFalse(length == len(df))

    # test that the text for the tweet is not longer than
    def test_length_of_tweet(self):
        length = len(self.df)
        print(self.df["from_user"])
        df = rf.textCheck(self.df)
        self.assertFalse(length == len(df))
