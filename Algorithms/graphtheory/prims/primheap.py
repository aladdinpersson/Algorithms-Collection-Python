# Prims algorithm for finding minimal spanning tree (MST) of a graph. Optimized version using Heaps!

# This code is functional but needs:
#   * Comments
#   * Clean up code a bit (loadgraph especially and new_node != None part could perhaps be cleaner)

# Aladdin Persson <aladdin.persson@hotmail.com>
#   2019-02-16 Initial programming

import heapq

def load_graph(file='edges.txt'):
    try:
        f = open(file, 'r')
    except IOError:
        raise("File does not exist!")

    line_list = f.readlines()

    num_nodes, num_edges = line_list[0].split()



    G = {line: [tuple(map(int, tup.split()))[::-1] for tup in line_list[1:]
                                if (int(tup.split()[0]) == line or int(tup.split()[1]) == line)]
                                for line in range(1, int(num_nodes) + 1)}


    f.close()
    return G, int(num_nodes)


def prims_algo(G, num_nodes):
    unvisited_nodes = [i for i in range(1, num_nodes + 1)]
    visited_nodes = []

    start = 1
    tot_cost = 0

    unvisited_nodes.remove(start)
    visited_nodes.append(start)
    MST = [start]

    heap = G[start]
    heapq.heapify(heap)

    while unvisited_nodes:
        (cost, n2, n1) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited_nodes and n2 in visited_nodes:
            new_node = n1

        elif n1 in visited_nodes and n2 in unvisited_nodes:
            new_node = n2

        if new_node != None:
            unvisited_nodes.remove(new_node)
            visited_nodes.append(new_node)
            MST.append(new_node)
            tot_cost += cost

            for each in G[new_node]:
                heapq.heappush(heap, each)

    return MST, tot_cost

if __name__ == '__main__':
    print('---- Computing minimal spanning tree using Prims Algorithm ---- \n')

    G, num_nodes = load_graph()
    print(f'Our loaded graph is: {G} \n')

    MST, tot_cost = prims_algo(G, num_nodes)

    print(f'The minimum spanning tree is:  {MST}')
    print(f'Total cost of minimum spanning tree is {tot_cost}')
