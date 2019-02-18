# Kruskal's algorithm for finding minimal spanning tree (MST) of a graph.
# Using Union find datastructure

# Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-18 Initial programming

# Comments: Might need some comments but I feel otherwise it is good implementation

from unionfind import unionfind

def load_graph(file='edges.txt'):
    G = []

    try:
        f = open(file, 'r')
    except IOError:
        raise("File does not exist!")

    line_list = f.readlines()

    num_nodes, num_edges = map(int,line_list[0].split())

    for line in line_list[1:]:
        G.append(tuple(map(int, line.split()))[::-1])

    return sorted(G), num_nodes


def kruskal(G):
    uf = unionfind(num_nodes)
    tot_cost, MST = 0, []

    for each_edge in G:
        cost, to_node, from_node = each_edge[0], each_edge[1], each_edge[2]

        if not uf.issame(from_node-1, to_node-1):
            tot_cost += cost
            uf.unite(from_node-1, to_node-1)
            MST.extend([from_node, to_node])

    return MST, tot_cost

if __name__ == '__main__':
    print('---- Computing minimal spanning tree using Kruskal\'s Algorithm ----')
    print()

    G, num_nodes = load_graph()

    print(f'Our loaded graph is: {G}')
    print()

    MST, total_cost = kruskal(G)

    print(f'Our minimum spanning tree is: {MST}')
    print(f'Total cost is: {total_cost}')