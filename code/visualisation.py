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
from wordcloud import WordCloud

#API request
apiKey = "AIzaSyCPCC8oAS-KmKp7PTSC3ZRwbsCqReR231I"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?key=" + apiKey + "&latlng=%s&sensor=true/false"

def plotTweetsPerHour(data):
    hours = list(data.keys())
    tweets = data.values()
    width = 1/1.5
    plt.bar(hours, tweets, width, color="blue")

    plt.show()

def plotTweetsPerDay(data):
    plt.plot([dt.date() for dt,num in data],
                [num for dt,num in data],
                linewidth = 5.0)
    plt.xlabel("dates of tweets")
    plt.ylabel("tweeets per day")
    plt.yscale("log")
    plt.gcf().autofmt_xdate()
    plt.show()

#Function that makes a pie chart given a list of labels and a list of sizes
def makePie(labels, sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


# Creates pie chart of the number of tweets, retweets and replies
# Reference: https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html
def plotStructure(df):
    labels = ["Original tweets", "Retweets", "Replies"]
    sizes = []

    sizes.append(an.getNumberOfOriginalTweets(df))
    sizes.append(an.getNumberOfRetweets(df))
    sizes.append(an.getNumberOfReplies(df))

    makePie(labels, sizes)

#Makes pir chart of the applications used to send the tweets
def plotApps(df):
    apps = an.getMostPopularApps(df)
    labels = []
    sizes = []

    for key in apps:
        labels.append(key)
        sizes.append(apps[key])

    makePie(labels, sizes)

def plotHashtagCloud(df):
    hashtags = an.getMostPopularHashtags(df, 100)
    plotWordCloud(hashtags)


def plotWordCloud(hashtags):
    wordcloud = WordCloud(
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(str(hashtags))  # {"a":10, "b": 30, "c": 3}

    print(wordcloud)
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
