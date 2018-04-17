# build plots/visualisations for:
# – the structure of the dataset (tweets/retweets/replies)
# – the timeline of the tweets activity
# – the word cloud for all other hashtags used in the tweets from the dataset
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from datetime import datetime
import analysis as an

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

def getTweetsAtTimeOfDay(df):
    hours = []
    

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
