# Purpose of Depth first search is (mainly from my understanding) to find if a graph G is connected.
# Identify all nodes that are reachable from a given starting node.

# Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-16 Initial programming


def DFS(G, curr_node, visited):
    """
    :param G: G = {from_node1:[to_node1, to_node2], from_node2: [to_node,] etc}
    :param curr_node: Node currently at, run from beginning this is the starting node
    :param visited: since it is recursive, visited is updated and needs to be sent in on recursive call
    :return: visited is initialized outside of DFS and updates this boolean array with which nodes has been visited
    """
    if visited[curr_node - 1]:
        return

    visited[curr_node - 1] = True

    neighbours = G[curr_node]

    for next_node in neighbours:
        DFS(G, next_node, visited)


# Small Eaxmple
# if __name__ == '__main__':
#      G = {1: [2], 2: [1, 3, 4], 3: [2], 4: [2, 5], 5: [4]}
#
#     visited = [False for i in range(1, len(G) + 1)]
#     start_node = 1
#
#     DFS(G, start_node, visited)
#
#     if any(visited) == False:
#         print("Result: This graph is connected!")
