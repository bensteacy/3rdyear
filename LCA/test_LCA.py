from unittest import TestCase
from LCA import LCA


class TestLCA(TestCase):

    def test_put_public(self):
        test_tree = LCA()
        self.assertEqual(test_tree.put_public(5, "A"), (5, "A"), "wrong")

    def test_put(self):
        self.fail()

    def test_size(self):
        self.fail()
