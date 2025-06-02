import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insertion_and_traversal(self):
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)
        self.assertEqual(self.bst.inorder_traversal(), [20, 30, 40, 50, 60, 70, 80])

    def test_search(self):
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))
        self.assertFalse(self.bst.search(20))

    def test_delete_leaf(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.delete(5)
        self.assertEqual(self.bst.inorder_traversal(), [10])

    def test_delete_node_with_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.delete(5)
        self.assertEqual(self.bst.inorder_traversal(), [2, 10])

    def test_delete_node_with_two_children(self):
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)
        self.bst.delete(30)
        self.assertEqual(self.bst.inorder_traversal(), [20, 40, 50, 60, 70, 80])

    def test_insert_duplicate(self):
        self.bst.insert(10)
        self.bst.insert(10)  # Should not insert again
        self.assertEqual(self.bst.inorder_traversal(), [10])

if __name__ == '__main__':
    unittest.main()
