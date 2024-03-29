import pandas as pd
import sys
import re

# Removes all rows that have null values
# if the null value is in a column where the minority of values are null
def removeNAN(df):
    for column in df:
        numOfNan = df[column].isnull().sum()
        if numOfNan < len(df[column]) / 2:
            df = df.dropna(subset=[column])
    return df

# Makes user_lang lowercase so that e.g. "en-gb" and "en-GB" are grouped together
# Converts all null value into english
# explained in the report
def langCheck(df):
    df["user_lang"] = df["user_lang"].fillna(value="en")
    df["user_lang"] = df["user_lang"].apply(lambda x: x.lower())
    return df

# Checks whether username is valid according to Twitter specifications
# remove username that are longer than 15 Characters
# remove usernames that are not alphanumeric (possibly containing an underscore)
def fromUserCheck(df):
    df = df[df["from_user"].map(len) < 15]
    df = df[df["from_user"].map(lambda x: re.search(r'[a-zA-Z0-9_]', x)) != None]
    return df


def nameValidator(x):
    return re.search(r'[a-zA-Z0-9_]', x)

# Drops all rows that have a text length exceeding 140 chars
# Retweets can be 160 characters
# 160 - 140 = 20, 20 extra characters for retweet (RT @<up to 15 chars>)
def textCheck(df):
    df = df[df["text"].map(len) <= 160]
    return df

# Creates new CSV file with the cleaned dataset
# This dataset is used in the analysis and viisualisation
def makeCSV(df):
    df.to_csv("../data/CometLanding_ref.csv", index=False)

# Function to refine data outside Jupyter Notebook
def cleanData(df):
    df = df.drop_duplicates(keep = False)
    df = langCheck(df)
    df = removeNAN(df)
    df = fromUserCheck(df)
    df = textCheck(df)
    return df

# This is for if the module is ran from the command line
if __name__ == "__main__":
    df=pd.read_csv("../data/CometLanding.csv")
    df = cleanData(df)
    makeCSV(df)
