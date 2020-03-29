'''
Prims algorithm for finding minimal spanning tree (MST) of a graph. Optimized version using Heaps!
If there is no MST because graph is disconnected then prim's algorithm will return the MST of the connected subgraph

Time Complexity: O(mlog(n))

Aladdin Persson <aladdin.persson@hotmail.com>
    2019-02-16 Initial programming
    2020-03-29 Changed few lines to be able to handle empty graphs, etc, and changed how MST is computed (now correctly)
'''

import heapq

def load_graph(file='edges.txt'):
    try:
        f = open(file, 'r')
    except IOError:
        raise("File does not exist!")

    line_list = f.readlines()

    num_nodes, num_edges = line_list[0].split()

    # We want to have edge cost first because the min heap will be based on edge cost
    # concretely that's why we do [::-1], a bit confusing maybe
    G = {line: [tuple(map(int, tup.split()))[::-1] for tup in line_list[1:]
                                if (int(tup.split()[0]) == line or int(tup.split()[1]) == line)]
                                for line in range(1, int(num_nodes) + 1)}

    f.close()
    return G

# Takes as input G which will have {node1: [(cost, to_node, node1), ...], node2:[(...)] }
def prims_algo(G, start=1):
    if len(G) == 0:
        return [], 0

    unvisited_nodes = [i for i in range(1, len(G) + 1)]
    visited_nodes = []
    tot_cost = 0

    unvisited_nodes.remove(start)
    visited_nodes.append(start)
    MST = []

    heap = G[start]
    heapq.heapify(heap)

    while unvisited_nodes:
        if len(heap) == 0:
            # there is no MST because graph is disconnected then return MST of subgraph
            return MST, tot_cost

        (cost, n2, n1) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited_nodes and n2 in visited_nodes:
            new_node = n1
            MST.append((n2, n1, cost))

        elif n1 in visited_nodes and n2 in unvisited_nodes:
            new_node = n2
            MST.append((n1, n2, cost))

        if new_node != None:
            unvisited_nodes.remove(new_node)
            visited_nodes.append(new_node)
            tot_cost += cost

            for each in G[new_node]:
                heapq.heappush(heap, each)

    return MST, tot_cost

if __name__ == '__main__':
    print('---- Computing minimal spanning tree using Prims Algorithm ---- \n')

    G = load_graph()
    MST, tot_cost = prims_algo(G)

    #print(f'The minimum spanning tree is:  {MST}')
    print(f'Total cost of minimum spanning tree is {tot_cost}')
