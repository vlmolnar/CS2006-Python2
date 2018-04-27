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
    # df = df.drop([df["text"].map(len) > 15])
    # df = df.drop([df["text"].map(nameValidator) == False])
    # df = list(filter(lambda x: len(x) <= 15, df["from_user"]))
    # df = list(filter(lambda x: re.search(r'[a-zA-Z0-9_]', x), df["from_user"]))
    # df[df["from_user"].apply(lambda x: len(x) <= 15) &
    # df["from_user"].apply(lambda x: re.search(r'[a-zA-Z0-9_]', x))]
    return df


def nameValidator(x):
    return re.search(r'[a-zA-Z0-9_]', x)

# Drops all rows that have a text length exceeding 140 chars
def textCheck(df):
    # df = df.drop([df["text"].map(len) > 140])
    # df = list(filter(lambda x: len(x) <= 140, df["text"]))
    # df[df["text"].apply(lambda x: len(x) <= 140)]
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
