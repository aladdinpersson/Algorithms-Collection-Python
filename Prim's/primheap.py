# Prims algorithm for finding minimal spanning tree (MST) of a graph

# This doesn't work atm

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
                                if int(tup.split()[0]) == line] for line in range(1, int(num_nodes) + 1)}

    # G = {int(line.split()[0]): [tuple(map(int, tup.split()))[::-1] for tup in line_list[1:]
    #                             if int(tup.split()[0]) == int(line.split()[0])] for line in line_list[1:]}

    f.close()
    return G, int(num_nodes)


def prims_algo(G, num_nodes):
    unvisited_nodes = [i for i in range(1, num_nodes + 1)]
    visited_nodes = []

    start = 1
    tot_cost = 0

    unvisited_nodes.remove(start)
    visited_nodes.append(start)

    heap = G[start]
    heapq.heapify(heap)

    while unvisited_nodes:
        #print(f'Length of unvisited nodes is {len(unvisited_nodes)}')

        #Can be confusing: n1 connects to n2, cost is the edge between them
        (cost, destination_node, origin_node) = heapq.heappop(heap)

        if destination_node in unvisited_nodes:
            unvisited_nodes.remove(destination_node)
            visited_nodes.append(destination_node)
            tot_cost += cost

            for each in G[destination_node]:
                heapq.heappush(heap, each)

    print(f'total cost is: {tot_cost}')



if __name__ == '__main__':
    print('Computing minimal spanning tree using Prims Algorithm')

    G, num_nodes = load_graph()
    print(f'Our loaded graph is: {G}')

    prims_algo(G, num_nodes)

    #print(f'total cost of minimum spanning tree is {tot_cost}')