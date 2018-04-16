# refine the dataset:
# - develop a procedure to check that the data match expected format and remove duplicates
# – in case of any inconsistencies and/or duplicates found, produce new file with refined data
#   to be used in the subsequent analysis
# – this step must be automated and documented in case one may need to re-run it, although it’s
#   not necessary to repeat it each time while re-running the analysis
import pandas as pd
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
    df[df["from_user"].apply(lambda x: len(x) <= 10) &
    df["from_user"].apply(lambda x: re.search(r'[a-zA-Z0-9_]', x))]
    return df

# Drops all rows that have a text length exceeding 140 chars
def textCheck(df):
    df[df["text"].apply(lambda x: len(x) <= 150)]
    return df

# Creates new CSV file with the cleaned dataset
def makeCSV(df):
    df.to_csv("../data/CometLanding_ref.csv", index=False)

# Function to clean data outside Jupyter Notebook
def cleanData(df):
    df=pd.read_csv("../data/CometLanding.csv")
    df = df.drop_duplicates(keep = False)
    df = rf.removeNAN(df)
    df = rf.langCheck(df)
    df = rf.fromUserCheck(df)
    df = rf.textCheck(df)
