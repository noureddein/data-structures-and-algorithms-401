

"""
! Tasks
    ? [1] Create a Linked List class

    ?[2] Within your Linked List class, include a head property.
        ?- Upon instantiation, an empty Linked List should be created.
        
    ?[3] The class should contain the following methods:

        ?[a] insert
        ?    - Arguments: value
        ?    - Returns: nothing
        ?    - Adds a new node with that value to the head of the list with an O(1) Time performance.

        ?[b] includes
        ?    - Arguments: value
        ?    - Returns: Boolean
        ?    - Indicates whether that value exists as a Nodes value somewhere within the list.

        ?[c] to string
        ?    Arguments: none
        ?    Returns: a string representing all the values in the Linked List, formatted as:
        ?    "{ a } -> { b } -> { c } -> NULL"

        ?[d] Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

        ?[e] Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        return ''

    def insert(self, new_node):
        """
            Insert method, take the input and add it after the head.
            Input:
                Node -> Type object
            Output:
                New node in linked list
        """
        try:
            new_node.next = self.head
            self.head = new_node
        except AttributeError:
            print("Check if you added yor value to a Node first.")

    def includes(self, value):
        """
            Includes method searching for a value in the linked list.
            If the value exist it return True, else return False.

            Input:
                Value -> Any
            Output:
                Boolean
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
            This method print all the items in the linked list.
        """
        current = self.head
        output = ''
        while current:
            output += "{{ {0} }} -> ".format(current.value)
            current = current.next
        output += "Null"
        return output


if __name__ == "__main__":
    from node import Node

    ll = LinkedList()
    ll.insert("A")
    ll.insert(Node('B'))
    ll.insert(Node('C'))
    ll.insert(Node('D'))
    print(ll)
    print(ll.to_string())
