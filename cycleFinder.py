# Just created this as a little project to find cycles in a graph
# There might be a better way to do this but I just brute forced it and it works pretty well


import numpy as np

alph = "ABCDEFGHIJKLMNOP"

def adjMatrix():
    nodes = int(input("Enter number of nodes: "))
    adj = [input(f"Enter paths from node {alph[i]}: ") for i in range(nodes)]
    adjmatr = np.zeros((nodes, nodes))
    for i, adjs in enumerate(adj):
        for j in adjs:
            adjmatr[i, alph.find(j)] = 1
    adjmatr = np.asmatrix(adjmatr)
    stop = ""
    counter = 1
    while stop.lower() == "":
        print(adjmatr**counter)
        stop = input("Enter stop to stop: ")
        counter += 1



def findCycles():
    nodes = int(input("Enter number of nodes: "))
    adj = [input(f"Enter paths from node {alph[i]}: ") for i in range(nodes)]
    totalMutes = []
    sMutes = []
    for i in range(nodes):
        x = mutesFinder(adj, alph[i], mutes = totalMutes, sortedMutes = sMutes)
        totalMutes = x[0]
        sMutes = x[1]
        
    print(f"{str(len(totalMutes))} cycles exist which are:\n" + " ".join(totalMutes))



def mutesFinder(adj, current, mutes=[], sortedMutes=[]): # Current is a string
    # use the last of current to find the options for next
    for i in adj[alph.find(current[-1])]:
        if i not in current:
            mutes, sortedMutes = mutesFinder(adj, current+i, mutes, sortedMutes)
        elif i == current[0] and "".join(sorted(current)) not in sortedMutes:
            sortedMutes.append("".join(sorted(current)))
            mutes.append(current+i)
    return (mutes, sortedMutes)

findCycles()