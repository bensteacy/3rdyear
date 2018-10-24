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


class DNode:
    def __init__(self, dkey, dvalue, dlevel, dparent=None,
                 dchildren=None):
        if dchildren is None:
            self.dchildren = []
        if dparent is None:
            self.dparent = []
        self.dvalue = dvalue
        self.dkey = dkey
        self.dlevel = dlevel


    def has_dchildren(self):
        if len(self.dchildren)>0:
            return True

    def return_dlevel(self):
        return self.dlevel

    def is_root_dnode(self):
        if self.dparent is not None:
            return True
    def size_dparent(self):
        return len(self.dparent)

    def size_dchildren(self):
        return len(self.dchildren)

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


class DAG:

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def insert_root(self, key, value):
        if not self.root:
            self.root = Node(key, value, 0)
        self.size = self.size + 1

    #def insert_DNode(self, key, value, level, parent_node, current_node):
     #   for i in range(0,current_node.size_children)

    def find_node(self, key, level, current_node):
        for i in range(0, current_node.size_dchildren-1):
            if current_node.key == key & current_node.level == level:
                return current_node
            elif current_node.has_dchildren:
                self.find_node(key, level, current_node.dchildren[i])
            elif:
                self.find_node(key, level, current_node.dchildren[i])






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
