from collections import Counter
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from datetime import datetime
import analysis as an
from wordcloud import WordCloud

# Returns bar chart to represent the number of tweets sent for each hour in the day
def plotTweetsPerHour(data):
    hours = list(data.keys())
    tweets = data.values()
    width = 1/1.5
    plt.bar(hours, tweets, width, color="blue")
    plt.xlabel("hour of day (24hr clock)")
    plt.ylabel("number of tweets")
    plt.show()

# Creates a line chart of tweet freuqency grouped by days
def plotTweetsPerDay(data):
    plt.plot([dt.date() for dt,num in data],
                [num for dt,num in data],
                linewidth = 5.0)
    plt.xlabel("dates of tweets")
    plt.ylabel("tweets per day")
    plt.yscale("log")
    plt.gcf().autofmt_xdate()
    plt.show()

# Function that makes a pie chart given a list of labels and a list of sizes
def makePie(labels, sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


# Creates pie chart of the number of tweets, retweets and replies
def plotStructure(df):
    labels = ["Original tweets", "Retweets", "Replies"]
    sizes = []

    sizes.append(an.getNumberOfOriginalTweets(df))
    sizes.append(an.getNumberOfRetweets(df))
    sizes.append(an.getNumberOfReplies(df))

    makePie(labels, sizes)

# Creates pie chart of the applications used to send the tweets
def plotApps(df):
    apps = an.getMostPopularApps(df)
    labels = []
    sizes = []

    for key in apps:
        labels.append(key)
        sizes.append(apps[key])

    makePie(labels, sizes)

# Creates a word cloud of the 100 most popular hashtags
def plotHashtagCloud(df):
    hashtags = an.getMostPopularHashtags(df, 100)
    plotWordCloud(hashtags)


# Creates a word cloud given a dictionary
# dictionary calculated form @analysis.getMostPopularHashtags
def plotWordCloud(hashtags):
    wordcloud = WordCloud(
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(str(hashtags))

    print(wordcloud)
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
