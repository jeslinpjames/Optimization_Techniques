"""
Algorithm:
1. Import necessary libraries: 
    - Import permutations from itertools module.
    - Import maxsize from sys module.

2. Define Function travellingSalesmanProblem(graph, n):
    - Initialize an empty list nodes to store all nodes except the starting node n.
    - Initialize minimumPath to the maximum possible integer value.
    - Generate permutations of all nodes except the starting node.
    - Iterate through each permutation:
        - Initialize currentPathWeight to 0.
        - Set k to the starting node n.
        - Iterate through each node j in the permutation:
            - Add the weight of the edge from node k to node j to currentPathWeight.
            - Update k to node j.
        - Add the weight of the edge from the last node in the permutation back to node n to currentPathWeight.
        - Update minimumPath with the minimum value between minimumPath and currentPathWeight.
    - Return minimumPath.

3. Main code:
    - Define the graph as a 2D array representing the weights of edges between nodes.
    - Define the starting node n.
    - Call travellingSalesmanProblem function with the graph and the starting node.
    - Print the minimum path weight.


"""

from itertools import permutations
from sys import maxsize

V = 4


def travellingSalesmanProblem(graph, n):

    nodes = []
    for i in range(V):
        if i != n:
            nodes.append(i)
    minimumPath = maxsize
    nextPermutation = permutations(nodes)
    for i in nextPermutation:
        currentPathWeight = 0
        k = n
        for j in i:
            currentPathWeight += graph[k][j]
            k = j
        currentPathWeight += graph[k][n]
        minimumPath = min(minimumPath, currentPathWeight)
    return minimumPath

if __name__ == "__main__":
    graph = [[0, 12, 18, 24], [12, 0, 36, 28], [18, 36, 0, 32], [24, 28, 32, 0]]
    n = 0
    minimumPathWeight = travellingSalesmanProblem(graph, n)
    print("Minimum Cost :", minimumPathWeight)
