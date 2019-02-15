import random, copy

random.seed(1)

def load_graph():
    data = open('data.txt', 'r')
    G = {}

    for line in data:
        lst = [int(x) for x in line.split()]
        G[lst[0]] = lst[1:]

    return G


def get_random_edge(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2


def karger_contraction(G):
    length = []

    while len(G) > 2:
        v1, v2 = get_random_edge(G)
        G[v1].extend(G[v2])

        for edge in G[v2]:
            G[edge].remove(v2)
            G[edge].append(v1)

        # self-connections
        while v1 in G[v1]:
            G[v1].remove(v1)

        del G[v2]

    for key in G.keys():
        length.append(len(G[key]))

    return length[0]


def main():
    count = None
    G = load_graph()
    N = 100

    for i in range(N):
        data = copy.deepcopy(G)
        min_cut = karger_contraction(data)
        if count == None or min_cut < count:
            count = min_cut

    return count

val = main()
print(val)