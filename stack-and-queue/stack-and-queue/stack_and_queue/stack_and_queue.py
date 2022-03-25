

class Node:
    """Class the create a new object that contain two properties Value and Next"""

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Value {self.value}"


class Stack:
    """The class create an object contain a linked nodes linearly."""

    def __init__(self, node=None) -> None:
        self.top = node

    def __str__(self) -> str:
        if self.top is not None:
            return f"< 'Stack' class with top value: {self.top.value} >"
        return "Stack empty!"

    def push(self, value):
        """
            Push method takes a value as an argument and make it a node.
            then change the top pointer to indicate to the last node.
            Input:
                Value -> Any
            Output:
                Return none
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
            The pop method delete the last node in the stack.
            and change the top pointer to the previous node.
            Input:
                None
            Output:
                Return none
        """
        if self.is_empty():
            return 'Stack empty'

        temp = self.top
        self.top = self.top.next
        temp.next = None

    def peek(self):
        """
            Peek method return the value of the top indicator.
            Input:
                None
            Output:
                Return value -> Any
        """
        if self.is_empty():
            return 'Stack empty'

        return self.top.value

    def is_empty(self):
        """Check if the top is empty and return a boolean value."""
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        if self.front != None and self.back != None:
            return f"< 'Queue' class with Front: {self.front.value} and Back: {self.back.value}  >"
        return "Queue is empty!"

    def enqueue(self, value):
        """
            Add a new node to the queue and change the indicators.
            The front indicate to the first node and the back indicate to the last node.

            Input:
                Value -> Any
            Output:
                Return none
        """
        node = Node(value)

        if self.front == None:
            self.front = node
            self.back = node

        self.back.next = node
        self.back = node

    def dequeue(self):
        """
            Delete a node from queue and change the front indicator to represent the next node.
            Input:
                None
            Output:
                None
        """
        is_empty = self.is_empty()
        if is_empty:
            return "Queue empty!"

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """Return the value of front indicator."""
        is_empty = self.is_empty()
        if is_empty:
            return "Queue empty!"

        return self.front.value

    def is_empty(self):
        """Check if the queue class empty, and return boolean value"""
        return self.front == None


queue_ = Queue()
queue_.enqueue(1)
queue_.enqueue(2)
queue_.enqueue(3)
# queue_.enqueue(4)
# queue_.enqueue(5)

stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')

print(queue_.peek())
