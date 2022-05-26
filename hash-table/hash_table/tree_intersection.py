from queue import Queue
from binarytree import build2, Node

if __name__ == "__main__":
    from hash_map import HashTable, CustomError
else:
    from hash_table.hash_map import HashTable


class TreeIntersection(HashTable):
    counter = 0

    def hash_tree(self, root):
        """The function take a tree, hashed the value and insert it into the hash table.

        INPUT --> object

        OUTPUT --> None
        """
        self.counter += 1
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            front = queue.get()
            key = f"{front.value}+{self.counter}"
            self.set(key, front.value)
            if front.left:
                queue.put(front.left)
            if front.right:
                queue.put(front.right)
            self.counter += 1

    def _validate_trees(self, trees=[]):
        "This function validate the type of trees."
        for tree in trees:
            if not isinstance(tree, Node):
                raise CustomError(TypeError("Tree not a type of node!"))

    def tree_intersection(self, tree_1, tree_2):
        """The function take two trees and loop through the tree_2 and compare it with tree_1
        to get the intersecting values at the same location, tree_1 passed to the hash_tree function.

        INPUT --> tree object

        OUTPUT --> list of intersecting values
        """
        self._validate_trees([tree_1, tree_2])
        self.hash_tree(tree_1)
        self.counter = 1
        result = []
        queue = Queue()
        queue.put(tree_2)
        while not queue.empty():
            front = queue.get()
            key = f"{front.value}+{self.counter}"
            tree_value = self.get(key)
            if tree_value == front.value:
                result.append(front.value)
            if front.left:
                queue.put(front.left)
            if front.right:
                queue.put(front.right)
            self.counter += 1
        return result


if __name__ == "__main__":

    ht = TreeIntersection(10)
    tree_1_values = [42, 100, 600, 15, 160, 200, 350, 125, 175, 4, 500]
    tree_2_values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]

    tree_1 = build2(tree_1_values)
    tree_2 = build2(tree_2_values)
    print(ht.tree_intersection(tree_1, tree_2))

    ht_cha = TreeIntersection(10)

    tree_3_values = ["A", "B", "C", "D"]
    tree_4_values = ["A", "F", "C", "H"]
    tree_3 = build2(tree_3_values)
    tree_4 = build2(tree_4_values)
    print(ht_cha.tree_intersection(tree_3, tree_4))
