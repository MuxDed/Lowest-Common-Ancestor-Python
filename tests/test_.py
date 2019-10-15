import unittest

from LCA_Project import findLCAUtil


class TestLCA (unittest.TestCase):
    def test_findLCAUtil(self):
        """
        Test that it can find LCA given n1 and n2
        """
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEqual(root, 2)


if __name__ == '__main__':
    unittest.main()
