class Node:
    def __init__(self, key, value, left=None, right=None,
                 parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.key = key

    def has_left_node(self):
        return self.left

    def has_right_node(self):
        return self.right

    def is_root_node(self):
        if self.parent is not None:
            return True


class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def put_public(self, key, value):
        if self.root:
            self.put_private(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size = self.size + 1

    def put_private(self, key, value, new_node):
        if key < new_node.key:
            if new_node.has_left_node():
                self.put_private(key, value, new_node.left)
            else:
                new_node.leftNode = Node(key, value, parent=new_node)
        else:
            if new_node.has_right_node():
                self.put_private(key, value, new_node.right)
            else:
                new_node.left = Node(key, value, parent=new_node)

    def find_lca(self, root_node, node1, node2):

        if root_node is None:
            return None

        if root_node.key > node1 and root_node.key > node2:
            return self.find_lca(root_node.left, node1, node2)

        if root_node.key > node2 and root_node.key > node1:
            return self.find_lca(root_node.right, node1, node2)

        return root_node.key

# test_tree = BST()
# test_tree.put_public(5, 7)
# test_tree.put_public(10, 7)
