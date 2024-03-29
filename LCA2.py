import networkx as nx


# Start functions


def lowest_common_ancestor_DAG(graph, a, b):
    if not isinstance(graph, nx.DiGraph):
        print("First parameter is expected to be a networkx Digraph.")
        return None

    if len(graph) == 0:
        print("This is an empty graph!")
        return None
    elif len(graph) == 1:
        print("Graph size 1.. ")
        return None

    if not graph.has_node(a):
        print(str(a) + " does not exist in the graph.")
        return None
    elif not graph.has_node(b):
        print(str(b) + " does not exist in the graph.")
        return None

    ancestorsA = nx.ancestors(graph, a)
    ancestorsB = nx.ancestors(graph, b)
    setA = set()
    setA.add(a)
    setB = set()
    setB.add(b)
    if bool(ancestorsB.intersection(setA)):
        lca = a
        return lca
    if bool(ancestorsA.intersection(setB)):
        lca = b
        return lca

    print("Node A: " + a)
    print("Node B: " + b)
    lca = None
    if a == b:
        lca = a
        print("Lowest common ancestor of " + a + " and " + b + " is: " + str(lca) + "!")
        print("")
        return lca

    if nx.topological_sort(graph).next() == a:
        lca = a
        print("Lowest common ancestor of " + a + " and " + b + " is: " + str(lca) + "!")
        print("")
        return lca

    node_a_parents = set()
    finished = 0
    temp = a
    while not finished:
        if len(list(graph.predecessors(temp))) != 0:
            node = graph.predecessors(temp).next()
            node_a_parents.add(node)
            temp = node
        else:
            finished = 1
    print("Parents of node A: " + str(node_a_parents))

    node_b_parents = set()
    finished = 0
    temp = b
    while not finished:
        if len(list(graph.predecessors(temp))) != 0:
            node = graph.predecessors(temp).next()
            node_b_parents.add(node)
            temp = node
        else:
            finished = 1
    print("Parents of node B: " + str(node_b_parents))

    # Find first intersection in set #B
    intersect = node_a_parents.intersection(node_b_parents)
    while bool(intersect):
        lca = intersect.pop()

    print("Lowest common ancestor of " + a + " and " + b + " is: " + str(lca) + "!")
    print("")
    return lca
# End functions
