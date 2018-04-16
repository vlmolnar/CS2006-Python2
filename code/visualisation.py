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
