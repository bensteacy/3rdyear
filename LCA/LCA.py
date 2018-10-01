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

    def put_public(self, key, value):
        if self.root:
            self.put_private(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size = self.size + 1

    def put_private(self, key, value, new_node):
        if key < new_node.key:
            if new_node.hasLeftNode():
                self.put_private(key, value, new_node.left)
            else:
                new_node.leftNode = Node(key, value, parent=new_node)
        else:
            if new_node.hasRightNode():
                self.put_private(key, value, new_node.right)
            else:
                new_node.left = Node(key, value, parent=new_node)

    def find_lca(root, node1, node2):

        route1 = []
        route2 = []
        find_route(root, route1, node1)
        find_route(root, route2, node2)
        x = 0
        while x < len(route1) and x < len(route2):
            if route1[x] != route2[x]:
                break
            x += 1
        return route1[x-1]

    def find_route(root, route, key):

        route.append(root.key)
        if ((root.left != None and find_route(root.left, route, key)) or
                (root.right != None and find_route(root.right, route, key))):
            return True



