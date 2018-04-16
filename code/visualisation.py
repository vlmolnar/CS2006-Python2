# build plots/visualisations for:
# – the structure of the dataset (tweets/retweets/replies)
# – the timeline of the tweets activity
# – the word cloud for all other hashtags used in the tweets from the dataset
from collections import Counter
import matplotlib as mpl
from dateutil import parser

def getTimesCreated(df):
    times = []
    for time in df["created_at"]:
        dt = parser.parse(time)
        times.append(dt)
    return times[:10]
    counter = Counter(time)
    popular = counter.most_common()
    #return popular[:5]
