"""
Author: Philip Andreadis
e-mail: philip_andreadis@hotmail.com

    This script implements a simple heuristic solver for the Traveling Salesman Problem.
    It is not guaranteed that an optimal solution will be found.

    Format of input text file must be as follows:
    1st line - number of nodes
    each next line is an edge and its respective weight

    The program is executed via command line with the graph in the txt format as input.

"""

import time
import sys



"""
This function reads the text file and returns a 2d list which represents 
the adjacency matrix of the given graph
"""
def parseGraph(path):
  # Read number of vertices and create adjacency matrix
  f = open(path, "r")
  n = int(f.readline())
  adjMatrix = [[-1 for i in range(n)] for j in range(n)]
  #Fill adjacency matrix with the correct edges
  for line in f:
    edge = line.split(" ")
    edge = list(map(int, edge))
    adjMatrix[edge[0]][edge[1]] = edge[2]
    adjMatrix[edge[1]][edge[0]] = edge[2]
  for i in range(len(adjMatrix)):
    adjMatrix[i][i] = 0
  return adjMatrix



"""
Returns all the neighboring nodes of a node sorted based on the distance between them.
"""
def rankNeighbors(node,adj):
    sortednn = {}
    nList = []
    for i in range(len(adj[node])):
        if adj[node][i]>0:
            sortednn[i] = adj[node][i]
    sortednn = {k: v for k, v in sorted(sortednn.items(), key=lambda item: item[1])}
    nList = list(sortednn.keys())
    return nList


"""
Function implementing the logic of nearest neighbor TSP.
Generate two lists a and b, placing the starting node in list a and the rest in list b.
While b is not empty append to a the closest neighboring node of the last node in a and remove it from b.
Repeat until a full path has been added to a and b is empty.
Returns list a representing the shortest path of the graph.
"""
def nnTSP(adj):
    nodes = list(range(0, len(adj)))
    #print(nodes)
    weight = 0
    global length
    # Starting node is 0
    a = []
    a.append(nodes[0])
    b = nodes[1:]
    while b:
        # Take last placed node in a
        last = a[-1]
        # Find its nearest neighbor
        sortedNeighbors = rankNeighbors(last,adj)
        # If node being checked has no valid neighbors and the path is not complete a dead end is reached
        if (not sortedNeighbors) and len(a)<len(nodes):
            print("Dead end!")
            return a
        flag = True
        # Find the neighbor that has not been visited
        for n in sortedNeighbors:
            if n not in a:
                nextNode = n
                flag = False
                break
        # If all neighbors of node have been already visited a dead end has been reached
        if flag:
            print("Dead end!")
            return a
        a.append(nextNode)
        b.remove(nextNode)
        # Add the weight of the edge to the total length of the path
        weight = weight + adj[last][nextNode]
    # Finishing node must be same as the starting node
    weight = weight + adj[a[0]][a[-1]]
    length = weight
    a.append(a[0])
    return a


if __name__ == "__main__":
  # Import graph text file
  filename = sys.argv[1]
  print("~Nearest Neighbor~")
  start = time.time()
  graph = parseGraph(filename)
  n = len(graph)
  length = 0

  # Print adjacency matrix
  print("Adjacency matrix of input graph:")
  for i in range(len(graph)):
      print(graph[i])

  start = time.time()

  path = nnTSP(graph)

  finish = time.time()-start

  # Output
  print("Path:",path)
  print("Length",length)
  print("Time:",finish)