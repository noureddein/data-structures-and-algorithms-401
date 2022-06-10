from queue import Queue as QueueInt


class TreeNode:
    """Create the tree node object."""

    def __init__(self, value):
        if value is None:
            raise CustomError("Tree node value can not be NONE!")
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root) -> None:
        if not isinstance(root, TreeNode):
            raise CustomError("Your input is not a type of Tree Node class!")
        self.root = root

    def pre_order(self):
        root = self.root

        def _walk(root, printed_values=[]):
            printed_values.append(root.value)
            if root.left is not None:
                _walk(root.left, printed_values)
            if root.right is not None:
                _walk(root.right, printed_values)
            return printed_values

        values = _walk(root)
        return values

    def in_order(self):
        root = self.root

        def _walk(root, printed_values=[]):
            if root.left is not None:
                _walk(root.left, printed_values)

            printed_values.append(root.value)

            if root.right is not None:
                _walk(root.right, printed_values)

            return printed_values

        values = _walk(root)
        return values

    def post_order(self):
        root = self.root

        def _walk(root, printed_values=[]):
            if root.left is not None:
                _walk(root.left, printed_values)
            if root.right is not None:
                _walk(root.right, printed_values)

            printed_values.append(root.value)
            return printed_values

        values = _walk(root)
        return values

    def get_tree_max(self):
        root = self.root
        queue = QueueInt()
        queue.put(root)
        max_val = 0
        while not queue.empty():
            front = queue.get()
            if not isinstance(front.value, int) and isinstance(front.value, float):
                raise CustomError("Your value is not a number!")
            if front.value > max_val:
                max_val = front.value

            if front.left is not None:
                queue.put(front.left)

            if front.right is not None:
                queue.put(front.right)

        return max_val


class BinarySearchTree(BinaryTree):
    def breadth_first(self):
        values = []
        queue = QueueInt()
        queue.put(self.root)
        while not queue.empty():
            front = queue.get()
            values.append(front.value)

            if front.left is not None:
                queue.put(front.left)

            if front.right is not None:
                queue.put(front.right)
        return values

    def add(self, value):
        values = []
        queue = QueueInt()
        queue.put(self.root)

        while not queue.empty():
            front = queue.get()
            values.append(front.value)

            if front.left is not None:
                queue.put(front.left)

            if front.left is None:
                front.left = TreeNode(value)
                break

            if front.right is not None:
                queue.put(front.right)

            if front.right is None:
                front.right = TreeNode(value)
                break
        return values

    def contains(self, value):
        queue = QueueInt()
        queue.put(self.root)
        while not queue.empty():
            front = queue.get()
            if front.value == value:
                return True
            if front.left is not None:
                queue.put(front.left)
            if front.right is not None:
                queue.put(front.right)
        return False


def in_order(root1, root2):
    def _walk(root, leafs_files=0):
        if root.left is None and root.right is None:
            leafs_files += 1

        if root.left is not None:
            _walk(root.left, leafs_files)

        if root.right is not None:
            _walk(root.right, leafs_files)

        return leafs_files

    leafs_root1 = _walk(root1)
    leafs_root2 = _walk(root2)
    if leafs_root1 == leafs_root2:
        return True
    return False


if __name__ == "__main__":
    import custom_error as CustomError
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    a.left = b
    b.left = d
    b.right = e

    a.right = c
    c.right = f

    tree = BinaryTree(a)
    print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    bst = BinarySearchTree(a)
    # print(bst.add("G"))
    # print(bst.add("H"))
    # print(bst.add("I"))
    # print(bst.add("J"))
    # print(bst.add("K"))
    # print(bst.contains(True))
