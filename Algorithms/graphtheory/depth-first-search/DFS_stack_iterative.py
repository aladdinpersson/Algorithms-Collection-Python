'''
Depth first search has many applications,for example finding if a graph G is connected.
Identify all nodes that are reachable from a given starting node.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
    2019-02-17 Initial programming
    2020-03-29 Cleaned up code, made test cases
'''


def load_graph(file='exgraph.txt'):
    data = open(file, 'r')
    G = {}

    for line in data:
        lst = [int(x) for x in line.split()]
        G[lst[0]] = lst[1:]

    num_nodes = len(G)

    return G, num_nodes

def DFS(G, start_node):
    visited = [False for i in range(1, len(G) + 1)]
    path = [start_node]
    stack = []
    stack.append(start_node)

    while stack:
        v = stack.pop()
        if not visited[v-1]:
            visited[v-1]=True

            for connected_node in G[v]:
                if not visited[connected_node-1]:
                    stack.append(connected_node)
                    path.append(connected_node)

    return visited, path

if __name__ == '__main__':
    G, num_nodes = load_graph()
    start_node = 1
    visited = DFS(G, start_node)

    if all(visited) == True:
        print("Return: This graph is connected!")
    else:
        print("Not all nodes were reachable, i.e the graph is not connected.")