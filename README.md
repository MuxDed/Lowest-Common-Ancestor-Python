# Lowest-Common-Ancestor-Python
• An implementation of LCA that works for a Binary Tree implementation and another one that works for a Direct acyclic graph
Assignment for CSU33012 Software Engineering year 3

LCA Binary Tree Function

Parameters: (root, node_a, node_b)
Description: This function will return the lowest common ancestor of node_a and node_b in the binary tree given.

LCA Directed Acyclic Graph Function

Parameters: (graph, a, b)
Description: This function will return the lowest common ancestor of A and B in the directed acyclic graph given.

binary_tree.py

Just a class for creating the binary tree.

test.py

A series of unit tests for the LCA functions, made with the unittest library.
To run these tests: python -m unittest -v test_LCA
