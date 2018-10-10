class Node:
    def __init__(self, key, value, level, children=None,
                 parent=None):
        if children is None:
            self.children = []
        self.parent = parent
        self.value = value
        self.key = key
        self.level = level

    def has_children(self):
        return self.children

    def return_level(self):
        return self.level

    def is_root_node(self):
        if self.parent is not None:
            return True


class DAG:

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def put_public(self, key, value, level):
        if self.root:
            self.put_private(key, value, level)
        else:
            self.root = Node(key, value)
        self.size = self.size + 1

    def put_private(self, key, value, new_node):
        if key < new_node.key:
            if new_node.has_left_node():
                self.put_private(key, value, new_node.left)
            else:
                new_node.left = Node(key, value, parent=new_node)
        else:
            if new_node.has_right_node():
                self.put_private(key, value, new_node.right)
            else:
                new_node.right = Node(key, value, parent=new_node)

    def find_lca(self, current_node, node1, node2):

        if self.root is None:
            return None

        if node1 == node2:
            return 

        if current_node.key > node1 and current_node.key > node2:
            return self.find_lca(current_node.left, node1, node2)

        if current_node.key > node2 and current_node.key > node1:
            return self.find_lca(current_node.right, node1, node2)

        return current_node.key

# test_tree = BST()
# test_tree.put_public(5, 7)
# test_tree.put_public(10, 7)
