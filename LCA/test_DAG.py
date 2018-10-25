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

        print("got this far")
