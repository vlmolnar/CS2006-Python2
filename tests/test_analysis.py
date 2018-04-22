from collections import Counter
import pandas as pd
import unittest
import json
import re

from code import analysis as an

class RefineTest(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv("/cs/home/js321/Documents/CS2006/python/P2/data/dummy_analysis.csv")

    # test getting the number of Retweets - tweets beginning with "RT @"
    # def test_get_num_retweets(self.df):
    #    length = 
