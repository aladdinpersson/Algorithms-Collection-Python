"""
Purpose is to find the shortest path between one source node to all other nodes using Bellman-Ford Algorithm.
The difference between Dijkstra and this is that this can handle negative edges. We do pay for this as it is
a lot slower than Dijkstra.

Time Complexity: O(mn)

Programmed by Aladdin Persson <aladdin dot persson at hotmail dot com>
  2019-03-04 Initial programming
"""


def bellman_ford(G, start):
    """
    :param G: {from_node1: {to_node1, cost1, to_node2, cost2}, from_node2: {etc}}
    :param start: node to start from
    """

    if len(G) == 0:
        raise ValueError("There should be something in the graph")

    # step1: initialize by setting to infinity etc.
    shortest_distance = {}
    predecessor = {}
    infinity = float("inf")

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
        for to_node, weight in G[from_node].items():
            if shortest_distance[from_node] + weight < shortest_distance[to_node]:
                shortest_distance[to_node] = -infinity

    return shortest_distance, predecessor


# if __name__ == '__main__':
#     G = {1: {2: -10, 3: 20},
#          2: {4: 40},
#          3: {4: 5},
#          4: {}}
#
#     print(f'Current graph is: {G}')
#     shortest, predecessor = bellman_ford(G, 1)
#     print(shortest)
