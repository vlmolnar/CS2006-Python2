from collections import Counter
import json
from dateutil import parser
from datetime import datetime
import pandas as pd
import re

# Returns number of unique tweets in dataset
def getNumberOfOriginalTweets(df):
    retweets = getNumberOfRetweets(df)
    replies = getNumberOfReplies(df)
    return len(df) - (retweets + replies)

# Returns the number of tweets that match a certain pattern
# This pattern identifies all the retweets
def getNumberOfRetweets(df):
    count = 0
    for i,row in df.iterrows():
        match = re.search("RT @", row["text"])
        if match != None:
            count += 1
    return count

# Returns the number of reply tweets
def getNumberOfReplies(df):
    return df["in_reply_to_user_id_str"].notnull().sum()

# Returns the total number of tweets
def getTotalTweetNumber(df):
    return getNumberOfRetweets(df) + getNumberOfOriginalTweets(df) + getNumberOfReplies(df)

# Returns the number of unique users in the dataset
def getNumberOfUniqueUsers(df):
    return len(df["from_user"].unique())

# the average number of tweets and replies sent by users
def averagesForData(df):
    users = getNumberOfUniqueUsers(df)
    averageTweetsPerUser = getNumberOfOriginalTweets(df) / users
    averageRetweetsPerUser = getNumberOfRetweets(df) / users
    averageRepliesPerUser = getNumberOfReplies(df) / users
    return (averageTweetsPerUser, averageRetweetsPerUser, averageRepliesPerUser)

# Prints results from function averagesForData(df)
def printAverages(df):
    tw, retw, rep = averagesForData(df)
    print("Average number of tweets per user", tw);
    print("Average number of retweets per user", retw);
    print("Average number of replies per user", rep);


# Prints data
def printAnalysis(df):
    print("Number of retweets:", getNumberOfRetweets(df))
    print("Number of replies:", getNumberOfReplies(df))
    print("Number of original tweets:", getNumberOfOriginalTweets(df))
    print("Number of tweets in total: ", getTotalTweetNumber(df))
    pop = getMostPopularHashtags(df, 5)
    print("most popular hashtags:")
    for tag,num in pop:
        print(tag,"-", num)

# This function appends all text in entities[hashtag] into a flat list
# Then it uses the counter in collection model to count frequencies
# Note: hashtags are not case sensitive
def getMostPopularHashtags(df, take):
    hashtags = []
    popular = []
    for entity in df["entities_str"]:
        data = json.loads(entity)
        for hashtag in data["hashtags"]:
            hashtags.append(hashtag["text"].lower())
    counter = Counter(hashtags)
    if take == -1:
        popular = counter.most_common()
    else:
        popular = counter.most_common(take)
    return popular

# Calls functions below to find 5 most popular apps and others
def getMostPopularApps(df):
    apps = getAppsUsed(df)
    return getPopularApps(5, apps)

# Returns dictionary of the applications used to send out tweets and the
# number of tweets sent on said application
def getAppsUsed(df):
    apps = {}
    for element in df["source"]:
        tokens = re.findall(r"[^><\/>]+", element) # r"[^><\/a>]"  [\w' ]+
        name = tokens[-2]
        if not name in apps:
            apps[name] = 1
        else:
            apps[name] += 1
    return apps

# Takes a dictionary and returns the "num" most popular, and groups all others together
def getPopularApps(num, apps):
    sortedkeys = []
    popular = {}
    othersVal = 0

    for a in sorted(apps, key=apps.get, reverse=True):
        sortedkeys.append(a)
    for i, elem in enumerate(sortedkeys):
        if i < num:
            popular[elem] = apps[elem]
        else :
            othersVal += apps[elem]
    popular["Other"] = othersVal
    return popular

# This function returns a list of tuples that are used to plot the number of
# tweets per day
def getTweetsPerDay(df):
    times = []
    day = parser.parse(df["created_at"][0])
    tweetsPerDay = 0
    for time in df["created_at"]:
        dt = parser.parse(time)
        if dt.day == day.day:
            tweetsPerDay += 1
        else:
            times.append((day, tweetsPerDay))
            day = dt
            tweetsPerDay = 1
    times.append((day, tweetsPerDay))
    return times

# This function returns a dict of the number of tweets per hour
# time zone is Pacific Time (PT)
def getTweetsAtTimeOfDayGlobal(df):
    hours = {}
    for time in df["created_at"]:
        dt = parser.parse(time)
        if dt.hour in hours:
            hours[dt.hour] += 1
        else:
            hours[dt.hour] = 1
    return hours

# This function returns a dict of the number of tweets per hour
# time zone is local time -- for this dataset the timezones were not provided
# therefore both graphs for the tweets per hour are the same
def getTweetsAtTimeOfDayLocal(df):
    hours = {}
    for time in df["time"]:
        dt = parser.parse(time)
        if dt.hour in hours:
            hours[dt.hour] += 1
        else:
            hours[dt.hour] = 1
    return hours
