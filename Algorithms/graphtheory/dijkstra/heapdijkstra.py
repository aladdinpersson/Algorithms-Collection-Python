"""
Dijkstra's algorithm for finding the shortest path.
Improved version with the usage of heaps.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
  2019-02-15 Initial coding
  2020-03-28 Small code changes, fixed for edge cases not covered

"""

import heapq


def make_graph(file):
    try:
        f = open(file, "r")
    except IOError:
        raise ("File does not exist!")

    line_list = f.readlines()

    # Kinda messy graph loading
    G = {
        int(line.split()[0]): {
            (int(tup.split(",")[0])): int(tup.split(",")[1])
            for tup in line.split()[1:]
            if tup
        }
        for line in line_list
        if line
    }
    f.close()
    return G


def dijkstra(G, start, end=None):
    if start not in G or (end != None and end not in G):
        return [], {end: float("inf")}

    distance, visited, history, heap, path = {}, {}, {}, [], []

    for node in G.keys():
        distance[node] = float("inf")
        visited[node] = False

    distance[start], visited[start] = 0, True
    heapq.heappush(heap, (0, start))

    while heap:
        (d, node) = heapq.heappop(heap)
        visited[node] = True

        for child_node, weight in G[node].items():
            if (not visited[child_node]) and (d + weight < distance[child_node]):
                history[child_node] = node
                distance[child_node] = d + weight
                heapq.heappush(heap, (distance[child_node], child_node))

    if end != None:
        current_node = end

        while current_node != start:
            try:
                path.insert(0, current_node)
                current_node = history[current_node]

            except KeyError:
                return [], distance

        path.insert(0, start)

    return path, distance


if __name__ == "__main__":
    # start, end = 1, 160
    # print(f'Goal is to find the path from node {start} to node {end}')
    # G = make_graph('dijkstraData.txt')

    G = {1: {2: 10, 3: 20}, 2: {4: 40}, 3: {4: 5}, 4: {}}
    start = 1
    end = 2

    path, dist = dijkstra(G, start, end)
    print(f"Path found: {path}")
    print(dist)
