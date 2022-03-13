

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
                New node in linked list.
        """
        try:
            new_node.next = self.head
            self.head = new_node
        except AttributeError:
            print("Check if you added yor value to a Node first.")

    def append(self, new_value):
        """
            The append method used to add a new node to the end of linked list.

            Input:
                Node -> Object
            Output:
                New node added to the end of the linked list.
        """
        current = self.head
        if self.head is None:
            self.head = new_value
            return
        while True:
            if current.next is None:
                current.next = new_value
                break
            current = current.next

    def insert_before(self, value, new_value):
        """
        The insert_before method took two arguments, and check if the value
        exist insert the new_value before it, if not will a print a string message.

        Input: 
            value -> The value to be checked and insert the new node before.

            new_value -> The node to be insert.
        Output:
            New node added to the linked list.
        """
        is_value_exist = self.includes(value)
        if is_value_exist:
            current = self.head
            prev_node = None
            while current:
                if current.value == value:
                    try:
                        prev_node.next = new_value
                    except AttributeError:
                        self.head = new_value
                        new_value.next = current
                        return
                    else:
                        new_value.next = current
                        return
                prev_node = current
                current = current.next
        return print('The value you want to insert before does not exist.')

    def insert_after(self, value, new_value):
        """
            The insert_after method used to insert a new node after the value specified.
            Input:
                Value -> The value to be insert the node after.
            Output:
                New node to the linked list.
        """
        is_value_exist = self.includes(value)
        if is_value_exist:
            current = self.head
            while current:
                if current.value == value:
                    new_value.next = current.next
                    current.next = new_value
                    return
                current = current.next
        return print('The value you want to insert after does not exist.')

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

    def delete_node(self, value):
        current_node = self.head
        prev_node = None
        while True:
            if current_node.value == value:
                try:
                    prev_node.next = current_node.next
                    break
                except AttributeError:
                    self.head = current_node.next
                    break
            if current_node.next == None:
                print('Not Found')
                break
            prev_node = current_node
            current_node = current_node.next


if __name__ == "__main__":
    from node import Node

    ll = LinkedList()
    ll.insert(Node("A"))
    ll.insert(Node('B'))
    ll.insert(Node('C'))
    ll.insert(Node('D'))
    # ll.append(Node('E'))
    # ll.append(Node('F'))
    # print(ll)
    # ll.insert_before("E", Node(333))
    # ll.insert_before(333, Node('A'))
    ll.insert_after('A', Node('JJ'))
    # ll.insert_before('B', Node('KK'))
    # ll.insert_after('A', Node('KKK'))
    print(ll.to_string())
    ll.delete_node('D')
    print(ll.to_string())
