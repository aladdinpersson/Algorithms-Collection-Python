'''
Purpose of this algorithm is finding a path that is in topological ordering for a directed acyclic graph (DAG).

Programmed by Aladdin Persson <aladdin.persson at hotmail.com>
*   2019-03-17 Intitial programming

'''

from collections import defaultdict, deque
import re

def load_graph(filename):
    graph = defaultdict(list)
    degree_incoming = defaultdict(int)

    for line in open(filename):
        from_node, to_node = [char.replace(' ', '') for char in re.findall(r' . ', line)]
        graph[from_node].append(to_node)
        degree_incoming[to_node] += 1

    return graph, degree_incoming

def toposort(graph, degree_incoming):
    curr_accessible_nodes = deque()

    for node in graph:
        if degree_incoming[node] == 0: curr_accessible_nodes.append(node)

    path = []

    while curr_accessible_nodes:
        node_topological = curr_accessible_nodes.popleft()
        path.append(node_topological)

        for connected_node in graph[node_topological]:
            degree_incoming[connected_node] -= 1

            if degree_incoming[connected_node] == 0:
                curr_accessible_nodes.append(connected_node)

    # Check if there are still incoming edges (meaning it will have cycles)
    for val in degree_incoming.values():
        if val != 0:
            raise ValueError("There are cycles in this graph!")

    return path

def main():
    # Note: The load graph WILL differ depending on the input graph you have.
    # There are many ways to have a textfile to describe a topological graph, and one needs to
    # adapt to the specific problem.
    graph, degree_incoming = load_graph('example.txt')
    path_to_take = toposort(graph, degree_incoming)
    print(f'One path to take that is a topological ordering is {"".join(path_to_take)}')

if __name__ == '__main__':
    main()