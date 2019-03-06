# Dijkstra's algorithm for finding the shortest path in a graph
# Programmed 2019-01-28 <aladdin.persson at hotmail dot com>

def make_graph(file):
    try:
        f = open(file, 'r')
    except IOError:
        raise("File does not exist!")

    line_list = f.readlines()

    # Found on mukeshmithrakumar github, thought this was clean..
    # populate the graph using data from the text file via dictionary comprehensions
    G = {int(line.split()[0]): {(int(tup.split(',')[0])): int(tup.split(',')[1])
                                for tup in line.split()[1:] if tup} for line in line_list if line}

    f.close()
    return G


def dijkstra(G, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = G
    infinity = float('inf')
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0


    while unseenNodes:
        minNode = None

        # priority-queue? -> Hittar bästa noden hittils
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node


        for childNode, weight in G[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode

        unseenNodes.pop(minNode)

    print("pred")
    print(predecessor)
    currentNode = end

    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)

    return path, shortest_distance[end]




#G = make_graph('dijkstraData.txt')

G =  {1:{2:10, 3:20},
      2:{4:40},
      3:{4:5},
      4:{}}
print(f'Current graph is: {G}')
path, shortest = dijkstra(G, 1, 4)

print(path)
print(shortest)
