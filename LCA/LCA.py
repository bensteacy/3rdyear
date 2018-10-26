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
    def __init__(self, dkey, dvalue, dlevel, dparent_val=None,
                 dchildren=None):
        if dchildren is None:
            self.dchildren = []
        if dparent_val is None:
            self.dparent = []
        else:
            self.dparent = []
            self.dparent.append(dparent_val)
        self.dvalue = dvalue
        self.dkey = dkey
        self.dlevel = dlevel

    def add_child(self, new_dnode):
        self.dchildren.append(new_dnode)

    def add_parent(self, new_dnode):
        self.dparent.append(new_dnode)

    def has_dparent(self):
        if len(self.dparent) > 0:
            return True
        else:
            return False

    def has_dchildren(self):
        if len(self.dchildren) > 0:
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

    def is_root_node(self):
        if self.dparent is None:
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
            self.root = DNode(key, value, 0)
        self.size = self.size + 1

    # def insert_DNode(self, key, value, level, parent_node, current_node):
    #   for i in range(0,current_node.size_children)
    def insert_node(self, key, value, level, parent_node_key, parent_node_level):
        parent_node = self.find_node(parent_node_key, parent_node_level)
        if parent_node is not None:
            new_node = DNode(key, value, level, parent_node)
            parent_node.add_child(new_node)
            self.size = self.size + 1
        else:
            print("No such parent value exists")

    def find_node(self, key, level):
        return self.find_node_private(key, level, self.root, path=None, visited=None)

    def find_node_private(self, key, level, current_node, path, visited):

        if visited is None:
            visited = []
        if path is None:
            path = []

        if current_node.dkey == key and current_node.dlevel == level:
            return current_node
        elif current_node.has_dchildren:
            if current_node not in visited:
                visited.append(current_node)
                path.append(current_node)
            j = len(current_node.dchildren)
            i = 0
            for i in range(i, j):
                if current_node.dchildren[i] not in visited:
                    return self.find_node_private(key, level, current_node.dchildren[i], path, visited)
            if current_node.has_dparent is False:
                print("No Value Exists")
                return None
            else:
                path.pop()
                prev_node = path[-1]
                return self.find_node_private(key, level, prev_node, path, visited)

    def find_path(self, key, level):
        return self.find_node_private(key, level, self.root, path=None, visited=None)

    def find_path_private(self, key, level, current_node, path, visited):

        if visited is None:
            visited = []
        if path is None:
            path = []

        if current_node.dkey == key and current_node.dlevel == level:
            return path
        elif current_node.has_dchildren:
            if current_node not in visited:
                visited.append(current_node)
                path.append(current_node)
            j = len(current_node.dchildren)
            i = 0
            for i in range(i, j):
                if current_node.dchildren[i] not in visited:
                    return self.find_node_private(key, level, current_node.dchildren[i], path, visited)
            if current_node.has_dparent is False:
                print("No Value Exists")
                return None
            else:
                path.pop()
                prev_node = path[-1]
                return self.find_node_private(key, level, prev_node, path, visited)

    def find_lca(self, node1, node2):

        if self.root is None:
            return None

        if node1 == node2:
            return
        an1 = self.find_ancestors(node1, node1, ancestor=None, path=None)
        an2 = self.find_ancestors(node2, node1, ancestor=None, path=None)
        intersect = [list(filter(lambda x: x in an1, sublist)) for sublist in an2]
        if intersect:
            if node1.level > node2.level:
                max_level = node1.level - 1
            else:
                max_level = node2.level - 1
            j = len(intersect)
            i = 0
            while max_level >= 0:
                for i in range(i, j):
                    current_node = range[i]
                    if current_node.dlevel == max_level:
                        return current_node.key, current_node.dlevel





        else:
            print("not related")
            return



    def find_ancestors(self, dnode, current_node, ancestor, path):
        if ancestor is None:
            ancestor = []
        if path is None:
            path = []

        if current_node.has_dparent:
            j = len(current_node.dparents)
            i = 0
            for i in range(i, j):
                if current_node.dparent[i] not in ancestor:
                    ancestor.append(current_node.dparent[i])
                    path.append(current_node.dparent[i])
                    return self.find_ancestors(dnode, current_node.dparent[i], ancestor, path)
            if current_node != dnode:
                path.pop()
                prev_node = path[-1]
                return self.find_ancestors(dnode, prev_node, ancestor, path)
            else:
                return ancestor







# test_tree = BST()
# test_tree.put_public(5, 7)
# test_tree.put_public(10, 7)
