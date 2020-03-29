# Purpose of Depth first search is (mainly from my understanding) to find if a graph G is connected.
# Identify all nodes that are reachable from a given starting node.

# Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-16 Initial programming

# Improvements:
#   * Check implementation with stack/queue

def load_graph(file='exgraph.txt'):
    data = open(file, 'r')
    G = {}

    for line in data:
        lst = [int(x) for x in line.split()]
        G[lst[0]] = lst[1:]

    num_nodes = len(G)

    return G, num_nodes


def DFS(G, curr_node, visited):
    if visited[curr_node - 1]:
        return

    visited[curr_node-1] = True

    # G is a dictionary
    neighbours = G[curr_node]

    for next_node in neighbours:
        DFS(G, next_node, visited)

if __name__ == '__main__':
    print('Loading graph and print:')

    try:
        G, num_nodes = load_graph()
        print(G)

    except TypeError:
        raise("Error loading graph.")

    # G = {1: [2], 2: [1, 3, 4], 3: [2], 4: [2, 5], 5: [4]}

    visited = [False for i in range(1, len(G) + 1)]
    start_node = 1

    DFS(G, start_node, visited)

    if any(visited) == False:
        print("Result: This graph is connected!")