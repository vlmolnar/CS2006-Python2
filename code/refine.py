import pandas as pd
import sys
import re

# Removes all rows that have null values if null is the minority of values for the given clumn
def removeNAN(df):
    for column in df:
        numOfNan = df[column].isnull().sum()
        if numOfNan < len(df[column]) / 2:
            df = df.dropna(subset=[column])
    return df

# Makes user_lang lowercase so that e.g. "en-gb" and "en-GB" are grouped together
def langCheck(df):
    df["user_lang"] = df["user_lang"].fillna(value="en")
    df["user_lang"] = df["user_lang"].apply(lambda x: x.lower())
    return df

# Checks whether username is valid according to Twitter specifications
def fromUserCheck(df):
    df = df[df["from_user"].map(len) < 15]
    df = df[df["from_user"].map(lambda x: re.search(r'[a-zA-Z0-9_]', x)) != None]
    return df

# Drops all rows that have a text length exceeding 140 chars
# 160 - 140 = 20, 20 extra characters for retweet (RT @<up to 15 chars>)
def textCheck(df):
    df = df[df["text"].map(len) <= 160]
    return df

# Creates new CSV file with the cleaned dataset
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

if __name__ == "__main__":
    df=pd.read_csv("../data/CometLanding.csv")
    df = cleanData(df)
    makeCSV(df)
