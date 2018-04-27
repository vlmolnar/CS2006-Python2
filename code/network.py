import networkx as nx
import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import re

#get all the nodes needed for the graph
# nodes are the uniqueue users
def getNodesOfUsers(df):
    return list(df["from_user"].unique())

# This function returns the lists for the edges in the network
# This function iterates the dataset and adds connections to the correct list
def getEdgesOfRetweets(df):
    count = 0
    retweet_edges = []
    mentions_edges = []
    replies_edge = []
    for i,row in df.iterrows():
        from_user = row["from_user"]
        # if reply
        if pd.notnull(row["in_reply_to_screen_name"]):
            replies_edge.append((from_user, row["in_reply_to_screen_name"]))

        words = row["text"].split(" ")
        for word in words:
            match = re.search("@", word)
            if match != None:
                index = words.index(word)
                user = words[index][1:]
                if words[index - 1] == "RT":     # if retweet
                    retweet_edges.append((from_user, user))
                else:
                    mentions_edges.append((from_user, user)) # if mention
    return retweet_edges, mentions_edges, replies_edge

# This function returns the graph built from the nodes and edges returned from
# the functions above.
def drawNetwork(df):
    nodes = getNodesOfUsers(df)
    retweet_edges, mentions_edges, replies_edge = getEdgesOfRetweets(df)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(retweet_edges)
    G.add_edges_from(mentions_edges)
    G.add_edges_from(replies_edge)
    for u,v in retweet_edges:
        G[u][v]['color'] = 'red'
    for u,v in mentions_edges:
        G[u][v]['color'] = "blue"
    for u,v in mentions_edges:
        G[u][v]['color'] = "green"
    remove = [node for node,degree in G.degree() if degree < 40]
    G.remove_nodes_from(remove)

    return G
