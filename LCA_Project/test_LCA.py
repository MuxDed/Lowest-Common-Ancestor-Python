import unittest

target = __import__("LowestCommonAncestor")

Node = target.Node
findLCAUtil = target.findLCAUtil
findLCA = target.findLCA


class TestLCA (unittest.TestCase):
    def test_findLCAUtil(self):
        """
        Test that it can find LCA given root and n1 and n2
                            1
                          /  \
                         2     3
                        / \   / \
                       4   5 6   7
         Binary tree structure for first test


        """

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # lca = findLCA(root, 4, 5)
        # print(lca)
        # self.assertEqual(lca, 2)
        self.assertEqual(findLCAUtil(root, 4, 5, 0), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()
