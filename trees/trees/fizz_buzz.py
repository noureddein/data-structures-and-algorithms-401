from queue import Queue
from trees.k_ary import KTreeNode
from trees.custom_error import CustomError


class FizzBuzz:
    def __init__(self, k_ary_tree) -> None:
        if not isinstance(k_ary_tree, KTreeNode):
            raise CustomError(
                "Your input is not a type of k-ary Trees Node object!")
        self.k_ary_tree = k_ary_tree

    def _fizz_buzz_logic(self, value):
        """
            Input -> number

            Output -> One of the following roles:
                If the value is divisible by 3, return “Fizz”

                If the value is divisible by 5, return “Buzz”

                If the value is divisible by 3 and 5, return “FizzBuzz”

                If the value is not divisible by 3 or 5, return the value as a string.
        """
        if not isinstance(value, int):
            raise CustomError('The value should be an integer number!')

        if value % 3 == 0 and value % 5 == 0:
            return 'FizzBuzz'
        if value % 3 == 0:
            return 'Fizz'
        if value % 5 == 0:
            return 'Buzz'
        return str(value)

    def fizz_buzz_tree(self):
        root = self.k_ary_tree
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            front = queue.get()
            front.value = self._fizz_buzz_logic(front.value)
            print(front.value)

            for child in front.children:
                queue.put(child)
        return root


if __name__ == '__main__':
    import custom_error as CustomError
    from k_ary import KTreeNode
    childrenNodes = [
        KTreeNode(1, [KTreeNode(4), KTreeNode(5)]),
        KTreeNode(2, [KTreeNode(6)]),
        KTreeNode(3, [KTreeNode(7)])
    ]
    k_ary = KTreeNode(0, childrenNodes)

    fizz_buzz = FizzBuzz(k_ary)
    fizz_buzz.fizz_buzz_tree()
