# build plots/visualisations for:
# – the structure of the dataset (tweets/retweets/replies)
# – the timeline of the tweets activity
# – the word cloud for all other hashtags used in the tweets from the dataset
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
from dateutil import parser
import analysis as an

def getTimesCreated(df):
    times = []
    for time in df["created_at"]:
        dt = parser.parse(time)
        times.append(dt)
    return times[:10]
    counter = Counter(time)
    popular = counter.most_common()
    #return popular[:5]

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
