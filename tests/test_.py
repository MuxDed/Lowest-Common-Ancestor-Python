import pytest

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def test_findLCA():
    lca = findLCA(root, 4, 5)
    if lca is not None:
        print "LCA(4, 5) = ", lca.key
    else :
        print "Keys are not present"

def test_findLCA2():
    lca = findLCA(root, 4, 10)
    if lca is not None:
        print "LCA(4,10) = "", lca.key
    else:
        print "Keys are not present"
