class Node:
    def __init__(self, key, value, left=None, right=None,
                 parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.key = key

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class LCA:

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def set_root(self, key, value):
        if self.root:
            self.put(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size = self.size + 1

    def put(self, key, value, new_node):
        if key < new_node.key:
            if new_node.hasLeftChild():
                self._put(key, value, new_node.leftChild)
            else:
                new_node.leftChild = Node(key, value, parent=new_node)
        else:
            if new_node.hasRightChild():
                self._put(key, value, new_node.rightChild)
            else:
                new_node.rightChild = Node(key, value, parent=new_node)


