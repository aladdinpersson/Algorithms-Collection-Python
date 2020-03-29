# Prims algorithm for finding minimal spanning tree (MST) of a graph

# With this straightforward implementation: O(m * n) where m = # edges, n = # vertices

# Aladdin Persson <aladdin.persson@hotmail.com>
#   2019-02-15 Initial programming

# Improvement: Want to implement using heap datastructure

def load_graph(path = 'edges.txt'):
    edge_list = []

    with open(path) as f:
        lines = f.readlines()
        num_nodes, num_edges = [int(i) for i in lines[0].split()]

        for line in lines[1:]:
            node1,node2,edge_cost = [int(i) for i in line.split()]
            edge_list.append( (node1,node2,edge_cost))

    return edge_list, num_nodes, num_edges

def prims_algo(edge_list, num_nodes):
    X = []
    V = [i for i in range(1, num_nodes + 1)]
    E = []
    total_cost = 0
    start = 1

    X.append(start)
    V.remove(start)

    while len(V) != 0:
        lowest_cost = float('inf')
        nodeX = None
        nodeV = None

        for edge in edge_list:
            if edge[0] in X and edge[1] in V:
                if edge[2] < lowest_cost:
                    nodeX = edge[0]
                    nodeV = edge[1]
                    lowest_cost = edge[2]

            elif edge[1] in X and edge[0] in V:
                if edge[2] < lowest_cost:
                    nodeX = edge[1]
                    nodeV = edge[0]
                    lowest_cost = edge[2]

        if nodeX != None:
            X.append(nodeV)
            V.remove(nodeV)
            E.append((nodeX, nodeV, lowest_cost))
            total_cost += lowest_cost

    return E, total_cost


if __name__ == '__main__':
    print('Computing minimal spanning tree using Prims Algorithm')

    edge_list, num_nodes, num_edges = load_graph()

    E, tot_cost = prims_algo(edge_list, num_nodes)


