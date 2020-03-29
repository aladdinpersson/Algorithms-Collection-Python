'''
Dijkstra's algorithm for finding the shortest path in a graph, this implementation
is a naive implementation, check my Heap implementation for a more efficient algorithm

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
    2019-01-28 Initial programming
    2020-03-28 Cleaned up code
'''

def dijkstra(G, start, end):
    '''
    :param G: {from_node1: {to_node1:cost1, to_node2:cost2}, from_node2 : {.., etc.}, ...}
    :param start: starting node
    :param end: ending node where we want to find path to
    :return: path from starting node to end node and the cost to get between them
    '''

    if start not in G or end not in G:
        return [], float('inf')

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

    # Find path from start node s to end node t
    currentNode = end

    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return [], float('inf')

    path.insert(0,start)


    return path, shortest_distance[end]


if __name__ == '__main__':
    G =  {1:{2:10, 3:20},
          2:{4:40},
          3:{4:5},
          4:{}}

    print(f'Current graph is: {G}')
    path, shortest = dijkstra(G, 1, 4)

    print(path)
    print(shortest)