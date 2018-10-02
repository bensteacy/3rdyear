from unittest import TestCase

from LCA import BST


class TestLCA(TestCase):

    def test_put_public(self):
        test_tree = BST()
        self.assertEqual(test_tree.put_public(5, "A"), (5, "A"), "wrong")
        self.assertEqual(test_tree.put_public(3, 7), (3, 7), "double wrong")

    def test_size(self):
        self.fail()
