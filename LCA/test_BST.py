from unittest import TestCase
from LCA import DAG


# test tree         //        _7_
#                   //      /     \
#                   //    _3_      8
#                   //  /     \
#                   // 1       6
# 	                //  \     /
# 	                //   2   4
# 	                //        \
# 	                //         5

class TestBST(TestCase):
    def test_put_public(self):
        test_tree = DAG()
        test_tree.put_public(7, 7)
        test_tree.put_public(8, 8)
        test_tree.put_public(3, 3)
        test_tree.put_public(1, 1)
        test_tree.put_public(2, 2)
        test_tree.put_public(6, 6)
        test_tree.put_public(4, 4)
        test_tree.put_public(5, 5)

    def test_find_lca(self):
        test_tree = DAG()
        test_tree.put_public(7, 7)
        test_tree.put_public(8, 8)
        test_tree.put_public(3, 3)
        test_tree.put_public(1, 1)
        test_tree.put_public(2, 2)
        test_tree.put_public(6, 6)
        test_tree.put_public(4, 4)
        test_tree.put_public(5, 5)
        self.assertEqual(test_tree.find_lca(test_tree.root, 2, 5), 3)
        self.assertEqual(test_tree.find_lca(test_tree.root, 8, 1), 7)



