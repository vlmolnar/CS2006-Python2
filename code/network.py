import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd
import re

#get all the nodes needed for the graph
def getNodesOfUsers(df):
    return list(df["from_user"].unique())

def get_edges_of_users(df):
    count = 0
    edges = []
    for i,row in df.iterrows():
        match = re.search("RT @", row["text"])
        if match != None:
            words = row["text"].split(" ")
            user = words[1][1:]
            from_user = row["from_user"]
            print("from", from_user, "user:", user)
            edges.append((user, from_user))
        if count == 10: break
        count += 1
    return

def drawSquare(G):
    corners = [1,2,3,4]
    edges = [(1,2), (2,3), (3,4), (4,1)]
    G.add_nodes_from(corners)
    G.add_edges_from(edges)

    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()
    drawSquare(G)
