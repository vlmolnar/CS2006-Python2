# This module is used to test the data refining functions used to
# clean the raw data provided for this practical
# It is used by the module: test.py

### CLEARER EXPLAINATIONS IN test_notebook ###

import unittest
import pandas as pd
import re

from code import refine as rf

# The location of the test data used to mimic the dataset for this practical
test_data = "./tests/data/test_data_refine.csv"

class RefineTest(unittest.TestCase):

    # load the data for this tests
    def setUp(self):
        self.df = pd.read_csv(test_data)

    # This function tests that all the rows that contain null values are dropped
    # This is only the case if the column that the null data resides in has a
    # minority of null values (e.g. df["x"].isnull().sum() < len(df["x"]) / 2)
    # The output of this test can be compared to the expected output at out/expected_...
    def test_drop_nan(self):
        first_len = len(self.df)
        df = rf.removeNAN(self.df)
        self.assertFalse(first_len == len(df)) # check that rows have been removed
        df.to_csv("tests/out/result_test_drop_nan.csv");

    # This function tests that where a row has a null value for "user_lang"
    # it is replaced with "en" - reasoning for this is in the notebook
    # and report
    # The output of this test can be compared to the expected output at out/expected_...
    def test_lang_nan_replace(self):
        #a null value present
        self.assertTrue(self.df["user_lang"].isnull().any())
        df = rf.langCheck(self.df)
        # nulls replaced with en
        self.assertFalse(df["user_lang"].isnull().any())
        df.to_csv("tests/out/result_test_lang_nan_replace.csv");

    # This function tests that all the username provided conform to the
    # limitations provided by twitter
    # Usernames must be alphanumeric (can contain underscore) and less than 15
    # Characters
    # The output of this test can be compared to the expected output at out/expected_...
    def test_username_legal(self):
        df = rf.removeNAN(self.df)
        length = len(df)
        df = rf.fromUserCheck(df)
        self.assertFalse(length == len(df)) # check that rows have been removed
        df.to_csv("tests/out/result_test_username_legal.csv");

    # This function tests that all the text for the tweets provided conform
    # to the limitations as set by the twitter API
    def test_length_of_tweet(self):
        df = rf.removeNAN(self.df)
        length = len(df)
        df = rf.textCheck(df)
        self.assertFalse(length == len(df)) # check that rows have been removed
        df.to_csv("tests/out/result_test_length_of_tweet.csv");
