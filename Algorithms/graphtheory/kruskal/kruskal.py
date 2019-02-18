# Kruskal's algorithm for finding minimal spanning tree (MST) of a graph.

# Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-16 Initial programming

# Improvements:
# * The for-loop inside Kruskal can be improved for sure. Not sure exactly how to do it though

import sys
sys.path.append('graphtheory/depth-first-search')
from DFS_stack_iterative import DFS


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
    MST = []
    tot_cost = 0
    temp_G = {key: [] for key in range(1, num_nodes + 1)}

    for each_set in G:
        temp_G[each_set[2]] += [each_set[1]]
        temp_G[each_set[1]] += [each_set[2]]

        visited, path = DFS(temp_G, each_set[2])

        if len(set(path)) == len(path):
            tot_cost += each_set[0]

            if each_set[2] not in MST:
                MST.append(each_set[2])

            if each_set[1] not in MST:
                MST.append(each_set[1])
        else:
            temp_G[each_set[2]].pop()
            temp_G[each_set[1]].pop()

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