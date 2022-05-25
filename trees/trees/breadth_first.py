from queue import Queue as QueueInt
from trees.binary_tree import TreeNode
from trees.custom_error import CustomError


def breadth_first(root):
    if not isinstance(root, TreeNode):
        raise CustomError('The root is not a type of TreeNode')

    values = []
    queue = QueueInt()
    queue.put(root)
    while not queue.empty():
        front = queue.get()
        values.append(front.value)

        if front.left is not None:
            queue.put(front.left)

        if front.right is not None:
            queue.put(front.right)
    return values


if __name__ == "__main__":
    from binary_tree import TreeNode
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
    c.left = f

    print(breadth_first(a))
