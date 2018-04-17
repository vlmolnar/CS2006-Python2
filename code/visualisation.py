# build plots/visualisations for:
# – the structure of the dataset (tweets/retweets/replies)
# – the timeline of the tweets activity
# – the word cloud for all other hashtags used in the tweets from the dataset
from collections import Counter
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from datetime import datetime
import analysis as an
import urllib.request
import json

#API request
apiKey = "AIzaSyCPCC8oAS-KmKp7PTSC3ZRwbsCqReR231I"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?key=" + apiKey + "&latlng=%s&sensor=true/false"

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

# needs to be dicussed
def getTweetsAtTimeOfDay(df):
    hours = []
    hour = 0
    tweetsAtHour
    #for time in df[""]

#gettting locations
def getLocationsOfUsers(df):
    for coords in df["geo_coordinates"]:
        if pd.notnull(coords) and coords != "loc: 0,0":
            latlong = coords[5:]
            resp = urllib.request.urlopen(apiURL % latlong)
            data = json.loads(resp.read().decode())
            # print(data)
            # break
            if len(data["results"]) > 0:
                print(data["results"][0]["address_components"][6])


def plotTweetsPerDay(data):
    plt.plot([dt.date() for dt,num in data],
                [num for dt,num in data],
                linewidth = 5.0)
    plt.xlabel("dates of tweets")
    plt.ylabel("tweeets per day")
    plt.yscale("log")
    plt.gcf().autofmt_xdate()
    plt.show()

# Creates pie chart of the number of tweets, retweets and replies
# Reference: https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html
def plotStructure(df):
    labels = "Original tweets", "Retweets", "Replies"
    sizes = []
    totalTweets = an.getTotalTweetNumber(df)
    sizes.append((an.getNumberOfOriginalTweets(df) / totalTweets) * 100)
    sizes.append((an.getNumberOfRetweets(df) / totalTweets) * 100)
    sizes.append((an.getNumberOfReplies(df) / totalTweets) * 100)

    # Debug
    print("Retweet %:", sizes[0])
    print("Reply %:", sizes[1])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
