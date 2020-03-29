'''
Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
    2019-02-17 Initial programming
    2020-03-29 Cleaned up code, removed load graph, I think a small example is sufficient
               and instead only have the BFS function.
'''

from collections import deque

def BFS(G, start_node=1):
    '''
    :param G: Graph with G = {from_node1:[to_node1, to_node2], from_node2: [to_node,] etc}
    :param start_node: starting node to run BFS from
    :return: returns visited boolean array and path in which order it visited them
    '''
    visited = [False for i in range(1,len(G)+1)]

    Q = deque()
    Q.append(start_node)

    path = []

    while Q:
        curr_node = Q.popleft()
        path.append(curr_node)

        if not visited[curr_node - 1]:
            visited[curr_node-1]=True

            for connected_node in G[curr_node]:
                if not visited[connected_node-1]:
                    Q.append(connected_node)

    return visited, path

# Small Example Run
# if __name__ == '__main__':
#     G = {1:[2,3], 2:[1,4], 3:[1,4],4:[]}
#     visited, path = BFS(G)
#
#     if all(visited) == True:
#         print("Return: This graph is connected!")

#     else:
#         print("Not all nodes were reachable, i.e the graph is not connected.")