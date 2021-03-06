from unittest import TestCase
from LCA import DAG


class TestDAG(TestCase):
    def test_insert_node(self):
        test_dag = DAG()
        test_dag.insert_root(3, 7)
        test_dag.insert_node(8, 8, 1, 3, 0)
        test_dag.insert_node(6, 7, 2, 3, 0)
        test_dag.insert_node(5, 9, 3, 8, 1)
        test_dag.insert_node(9, 6, 4, 3, 0)
        test_dag.insert_node(11, 5, 4, 8, 1)
        test_dag.insert_node(11, 5, 6, 11, 4)
        # test_dag.insert_node(11, 5, 6, 8, 7)

    def test_find_lca(self):
        test_dag = DAG()
        test_dag.insert_root(3, 7)
        test_dag.insert_node(8, 8, 1, 3, 0)
        test_dag.insert_node(6, 7, 2, 3, 0)
        test_dag.insert_node(5, 9, 3, 8, 1)
        test_dag.insert_node(9, 6, 4, 3, 0)
        test_dag.insert_node(11, 5, 4, 8, 1)
        test_dag.insert_node(11, 5, 6, 11, 4)
        node1 = test_dag.find_node(11, 6)
        node2 = test_dag.find_node(9, 4)
        node3 = test_dag.find_node(5, 3)
        node4 = test_dag.find_node(11, 4)
        test_dag.find_lca(node1, node2)
        self.assertEqual(test_dag.find_lca(node1, node2), (3, 0))

        self.assertEqual(test_dag.find_lca(node3, node4), (8, 1))
