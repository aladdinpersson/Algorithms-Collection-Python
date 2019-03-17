'''
Purpose is to find the shortest path between one source node to all other nodes using Bellman-Ford Algorithm.
The difference between Dijkstra and this is that this can handle negative edges. We do pay for this as it is
a lot slower than Dijkstra.

Programmed by Aladdin Persson <aladdin dot persson at hotmail dot com>
  2019-03-04 Initial programming
'''

def make_graph(file):
    try:
        f = open(file, 'r')
    except IOError:
        raise IOError("File does not exist!")

    line_list = f.readlines()

    G = {int(line.split()[0]): {(int(tup.split(',')[0])): int(tup.split(',')[1])
                                for tup in line.split()[1:] if tup} for line in line_list if line}

    f.close()

    return G


def bellman_ford(G, start):
    if len(G) == 0:
        raise ValueError("There should be something in the graph")

    # step1: initialize by setting to infinity etc.
    shortest_distance = {}
    predecessor = {}
    infinity = float('inf')

    for node in G:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0
    num_vertices = len(G)

    # step2: relax edges
    for _ in range(num_vertices - 1):
        for from_node in G:
            for to_node, weight in G[from_node].items():

                if shortest_distance[from_node] + weight < shortest_distance[to_node]:
                    shortest_distance[to_node] = shortest_distance[from_node] + weight
                    predecessor[to_node] = from_node

    # step3: check neg. cycles
    for from_node in G:
        for to_node,weight in G[from_node].items():
            if shortest_distance[from_node] + weight < shortest_distance[to_node]:
                shortest_distance[to_node] = -infinity

    return shortest_distance, predecessor

if __name__ == '__main__':
    # G = make_graph('data.txt')

    G = {1: {2: -10, 3: 20},
         2: {4: 40},
         3: {4: 5},
         4: {}}

    print(f'Current graph is: {G}')
    shortest, predecessor = bellman_ford(G, 1)
    print(shortest)