import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd
import re

#get all the nodes needed for the graph
def getNodesOfUsers(df):
    return list(df["from_user"].unique())

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
                    mentions_edges.append((from_user, user))
    return retweet_edges, mentions_edges, replies_edge

def drawNetwork(df):
    nodes = getNodesOfUsers(df)
    retweet_edges, mentions_edges, replies_edge = getEdgesOfRetweets(df)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(retweet_edges)
    G.add_edges_from(mentions_edges)
    G.add_edges_from(replies_edge)
    for u,v in retweet_edges:
        G[u][v]['color'] = "red"
    # [G[u][v]['color'] = "blue" for u,v in mentions_edges]
    # [G[u][v]['color'] = "green" for u,v in replies_edge]

    nx.draw(G)
    plt.show()
    return

def drawSquare(G):
    corners = [1,2,3,4]
    edges = [(1,2), (2,3), (3,4), (4,1)]
    G.add_nodes_from(corners)
    G.add_edges_from(edges, color='b')

    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()
    drawSquare(G)
