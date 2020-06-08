"""
Purpose of this algorithm is finding a path that is in topological ordering for a directed acyclic graph (DAG).
If the graph is not a DAG and includes cycles it will return is_DAG = 'False' meaning it has cycles.

Time Complexity: O(n + m), n = |V|, m = |E|

Programmed by Aladdin Persson <aladdin.persson at hotmail.com>
*   2019-03-17 Intitial programming
*   2020-03-28 Removed load graph function, just having topological sort seems to make more sense
               The loading of the graph is so varying depending on input, doesn't make much sense to include it

"""

from collections import defaultdict, deque


def topological_ordering(graph, degree_incoming):
    if len(graph) == 0:
        return [], False

    curr_accessible_nodes = deque()

    for node in graph:
        if degree_incoming[node] == 0:
            curr_accessible_nodes.append(node)

    path = []

    while curr_accessible_nodes:
        node_topological = curr_accessible_nodes.popleft()
        path.append(node_topological)

        for connected_node in graph[node_topological]:
            degree_incoming[connected_node] -= 1

            if degree_incoming[connected_node] == 0:
                curr_accessible_nodes.append(connected_node)

    # Check if there are still incoming edges (meaning it will have cycles)
    is_DAG = True

    for val in degree_incoming.values():
        if val != 0:
            is_DAG = False
            path = []

    return path, is_DAG


if __name__ == "__main__":
    G = {"A": ["B"], "B": ["C", "D"], "C": ["D"], "D": []}
    degree_incoming = defaultdict(int, {"B": 1, "C": 1, "D": 2})

    print("The graph to check is : " + str(G))
    print("Which has incoming edges: " + str(degree_incoming))
    print("\n")
    path_to_take, is_DAG = topological_ordering(G, degree_incoming)
    print("The graph has a topological ordering <--> G is a DAG: " + str(is_DAG))
    print(f'One path to take that is a topological ordering is {"".join(path_to_take)}')
