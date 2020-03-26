[![Build Status](https://travis-ci.com/AladdinPerzon/Algorithms-Collection-Python.svg?branch=master)](https://travis-ci.com/AladdinPerzon/Algorithms-Collection-Python) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Algorithms Collection Python
Whenever I face an interesting problem I document the algorithm that I learned to solve it. Hopefully my list will increase as time goes on.

# Dynamic Programming
* [Knapsack 0/1](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/knapsack/knapsack_bottomup.py)  **O(nC) Bottom-Up implementation (Loops)**
* [Knapsack 0/1](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/knapsack/knapsack_memoization_recursive_topdown.py) **O(nC) - Recursive with memoization implementation**
* [:movie_camera:](https://youtu.be/XmyxiSc3LKg)[Sequence Alignment](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/sequence_alignment.py) **O(nm)**
* [:movie_camera:](https://youtu.be/dU-coYsd7zw)[Weighted Interval Scheduling](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/weighted_interval_scheduling.py) **O(nlog(n))**

# Graph theory
* [Kahns Topological Sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kahns-toposort/kahns.py) **- O(|V|+|E|)**
* [Bellman-Ford Shortest Path](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/bellman-ford/bellman_ford.py) **- Unoptimized implementation**
* [Floyd-Warshall Shortest Path](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/floyd-warshall/floyd-warshall.py) **- O(n<sup>3</sup>)**
* [Dijkstra Shortest Path](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/dijkstra/djikstra.py) **- Naive implementation**
* [Dijkstra Shortest Path](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/dijkstra/heapdijkstra.py) **O(|E| + |V|log|V|) - Heap implementation**
* [Karger's Minimum cut](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kargers/kargermincut.py)
* [Prim's Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/prims/prims_algorithm.py) **- Naive implementation**
* [Prim's Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/prims/primheap.py) **- Heap implementation**
* [Kruskal's Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kruskal/kruskal.py) **- Naive implementation**
* [Kruskal's Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kruskal/kruskal_unionfind.py) **- Union Find implementation**
* [Breadth First Search](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/breadth-first-search/BFS_queue_iterative.py) **O(|V| + |E|) - Queue Implementation**
* [Depth First Search](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/depth-first-search/DFS_stack_iterative.py) **O(|V| + |E|) - Stack Implementation**
* [Depth First Search](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/depth-first-search/DFS_recursive.py) **O(|V| + |E|) - Recursive Implementation**

# Mathematics
### Algebra
* [Karatsuba Multiplication](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/karatsuba/karatsuba.py) **- O(n<sup>1.585</sup>)** 
* [Intersection of two sets](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/intersection_of_two_sets/intersection_of_two_sets.py) **- O(nlog(n)) + O(mlog(m))** 
* [Union of two sets](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/union_of_two_sets/union_of_two_sets.py) **- O(nlog(n)) + O(mlog(m))** 

### Number Theory
* [Pollard p-1 factorization](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/pollard_p1/pollard_p1.py)  
* [Euclidean Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/euclid_gcd/euclid_gcd.py)  **- O(log(n))**
* [Extended Euclidean Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/extended_euclidean_algorithm/euclid_gcd.py)  **- O(log(n))**
* [Sieve of Eratosthenes](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/sieve_of_eratosthenes/sieve_eratosthenes.py) **- O(nlog(log(n)))**
* [Prime factorization](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/math/prime_factorization/primefactorization.py) **- O(sqrt(n))**

### Cryptography
* [Ceasar Cipher](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/ceasar_shifting_cipher/ceasar_shift_cipher.py)
* [Hill Cipher](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/hill_cipher/hill_cipher.py)
* [Vigenere Cipher](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py)
* [One time pad](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/one_time_pad/one_time_pad.py)
* [RSA-Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/RSA_algorithm/RSA.py)


### Numerical Methods
* [Bisection Method](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/numerical_methods/bisection.py)
* [(simple) Fixpoint iteration](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/numerical_methods/fixpoint.py)

# Other
* [Maintaining Median](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/other/median_maintenance.py)
* [Huffman Algorithm](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/other/Huffman/Huffman.py)
* [:movie_camera:](https://youtu.be/SmPxC8m0yIY)[Interval Scheduling](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/other/interval_scheduling.py) **- O(nlog(n))**
* [Binary Search](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/search/binarysearch.py) **- O(log(n))** 

# Sorting algorithms
* [Bubble sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/bubblesort.py) **- O(n<sup>2</sup>)** 
* [Hope sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/hopesort.py) **- O(1), hopefully**
* [Insertion sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/insertionsort.py) **- O(n<sup>2</sup>)** 
* [Selection sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/selectionsort.py) **- O(n<sup>2</sup>)** 
* [Merge sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/mergesort.py) **- O(nlog(n))** 
* [Randomized Quick sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/randomized_quicksort.py) **- Average O(nlogn) (Input independent!)**
* [Quick sort](https://github.com/AladdinPerzon/Algorithms-Collection-Python/blob/master/Algorithms/sorting/quicksort.py) **- Average O(nlog(n))**

# Contributing
I appreciate feedback on potential improvements and/or if you see an error that I've made!


