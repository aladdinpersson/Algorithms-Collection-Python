from collections import deque

def load_graph(file='exgraph.txt'):
    data = open(file, 'r')
    G = {}

    for line in data:
        lst = [int(x) for x in line.split()]
        G[lst[0]] = lst[1:]

    num_nodes = len(G)

    return G, num_nodes

def BFS(G, start_node=1):
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



if __name__ == '__main__':
    G, num_nodes = load_graph()
    # G = {1:[2,3], 2:[1,4], 3:[1,4],4:[]}

    visited, path = BFS(G)

    if all(visited) == True:
        print("Return: This graph is connected!")
    else:
        print("Not all nodes were reachable, i.e the graph is not connected.")


