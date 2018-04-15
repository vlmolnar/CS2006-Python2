# – calculate the total number of tweets, retweets and replies in the dataset
# – calculate the number of different users tweeting in this dataset
# – calculate the average number of tweets, retweets and replies sent by a user
# – identify most popular hashtags

from collections import Counter#
import json
import pandas as pd
import re

# return total number of tweets and retweets and replies in dataset
def getTotalNumberOfTweets(df):
    retweets = getNumberOfRetweets(df)
    replies = getNumberOfReplies(df)
    return len(df) - (retweets + replies)

# returns the number of tweets that match a certain pattern
def getNumberOfRetweets(df):
    count = 0
    for i,row in df.iterrows():
        match = re.search("RT @", row["text"])
        if match != None:
            count += 1
    return count

# return the number of tweets that were replies
def getNumberOfReplies(df):
    return df["in_reply_to_user_id_str"].notnull().sum()

# number of tweets defined as number of unique id's in the dataset
def getNumberOfUniqueUsers(df):
    return len(df["from_user"].unique())

# the average number of tweets and replies sent by a user
#
#   NEED TO DISCUSS!!!!
#
def averagesForData(df):
    users = getNumberOfUniqueUsers(df)
    averageTweetsPerUser = getTotalNumberOfTweets(df) / users
    averageRetweetsPerUser = getNumberOfRetweets(df) / users
    averageRepliesPerUser = getNumberOfReplies(df) / users
    return averageTweetsPerUser


# print data
def printAnalysis(df):
    print("Number of Retweets:", getNumberOfRetweets(df))
    print("Number of replies:", getNumberOfReplies(df))
    print("Number of tweets:", getTotalNumberOfTweets(df))
    pop = getMostPopularHashtags(df, 5)
    print("most popular hashtags:")
    for tag,num in pop:
        print(tag,"-", num)

def getMostPopularHashtags(df, take):
    hashtags = []
    for entity in df["entities_str"]:
        data = json.loads(entity)
        for hashtag in data["hashtags"]:
            hashtags.append(hashtag["text"])
    counter = Counter(hashtags)
    popular = counter.most_common(take)
    return popular
