"""
Purpose is to the find shortest path from all nodes to all other nodes, O(n^3).
Can be used with negative weights, however to check if it has negative cycles, bellman ford should prob. be used first.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-03-08 Initial programming

"""


def load_graph(file_name):
    try:
        with open(file_name) as file:
            line_list = file.readlines()
            file.close()

    except IOError:
        raise IOError("File does not exist")

    G = {
        int(line.split()[0]): {
            (int(tup.split(",")[0])): int(tup.split(",")[1])
            for tup in line.split()[1:]
            if tup
        }
        for line in line_list
        if line
    }

    # If we have path set path else make value infinity
    adjacency_matrix = [
        [
            G[i][j] if (i in G and j in G[i]) else float("inf")
            for j in range(1, len(G) + 1)
        ]
        for i in range(1, len(G) + 1)
    ]

    # Make diagonal values all 0
    for i in range(len(G)):
        adjacency_matrix[i][i] = 0

    # next will be matrix showing which path to take for the shortest path
    next = [
        [j if adjacency_matrix[i][j] != float("inf") else None for j in range(len(G))]
        for i in range(len(G))
    ]

    return adjacency_matrix, next


def floyd_warshall(adj_matrix, next):
    n = len(adj_matrix)
    # make a copy of adj_matrix, dp will contain APSP (All-Path-Shortest-Path) solutions,
    APSP = adj_matrix.copy()

    # Can we get a better path by going through node k?
    for k in range(n):
        # Goal is to find path from i to j
        for i in range(n):
            for j in range(n):
                # if distance from  i to k, then k to j is less than distance i to j
                if APSP[i][k] + APSP[k][j] < APSP[i][j]:
                    APSP[i][j] = APSP[i][k] + APSP[k][j]
                    next[i][j] = next[i][k]

    # return APSP (All-Path-Shortest-Path) matrix
    return APSP, next


def construct_path_to_take(next, start, end):
    go_through = start
    path = [start]

    while next[go_through][end] != end:
        go_through = next[go_through][end]
        path.append(go_through)

    path.append(end)

    return path


if __name__ == "__main__":
    adj_matrix, next = load_graph("test_graph.txt")
    APSP, next = floyd_warshall(adj_matrix, next)

    print(f"The shortest paths are {APSP}")
    print(f"The path to take is given by {next}")

    path_to_take = construct_path_to_take(next, 0, 3)
    print(path_to_take)
