
from queue import Queue


class KTreeNode:
    """Create the k-ary tree node object."""

    def __init__(self, value, children=[]):
        if value is None:
            raise CustomError("Tree node value can not be NONE!")
        self.value = value
        self.children = children


class KTreeArray:
    def __init__(self, root) -> None:
        if not isinstance(root, KTreeNode):
            raise CustomError(
                "Your input is not a type of k-ary Trees Node object!")
        self.root = root

    def breadthFirst(self):
        root = self.root
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            front = queue.get()
            print(front.value)

            for child in front.children:
                queue.put(child)


if __name__ == '__main__':
    import custom_error as CustomError
    childrenNodes = [
        KTreeNode('B', [KTreeNode('E'), KTreeNode('F')]),
        KTreeNode('C', [KTreeNode('G')]),
        KTreeNode('D', [KTreeNode('H')])
    ]
    k_ary = KTreeNode('A', childrenNodes)

    k_tree_array = KTreeArray(k_ary)
    k_tree_array.breadthFirst()
