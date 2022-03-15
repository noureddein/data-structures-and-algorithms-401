class LinkedList:
    ll_length = 0

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        return ""

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
            self.ll_length += 1
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
        if self.head is None:
            self.head = new_value
            self.ll_length += 1
            return
        current = self.head
        while True:
            if current.next is None:
                current.next = new_value
                self.ll_length += 1
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

        current = self.head
        prev_node = None
        while current:
            if current.value == value:
                try:
                    prev_node.next = new_value
                except AttributeError:
                    self.head = new_value
                    new_value.next = current
                    self.ll_length += 1
                    return
                else:
                    new_value.next = current
                    self.ll_length += 1
                    return
            prev_node = current
            current = current.next
        return print("The value you want to insert before does not exist.")

    def insert_after(self, value, new_value):
        """
        The insert_after method used to insert a new node after the value specified.
        Input:
            Value -> The value to be insert the node after.
        Output:
            New node to the linked list.
        """
        current = self.head
        while current:
            if current.value == value:
                new_value.next = current.next
                current.next = new_value
                self.ll_length += 1
                return
            current = current.next
        return print("The value you want to insert after does not exist.")

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
        output = ""
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
                    self.ll_length -= 1
                    break
                except AttributeError:
                    self.head = current_node.next
                    self.ll_length -= 1
                    break
            if current_node.next == None:
                print("Not Found")
                break
            prev_node = current_node
            current_node = current_node.next

    def kthFromEnd(self, k):
        """
        kthFromEnd method used to get the value of a specific position.

        Input:
            k -> integer, positive number
        Output:
            Return -> The value of that postion if it exist.

        """
        if k < 0 or type(k) is not int:
            return "Negative numbres or non-integer numbers not acceptable."

        if k > self.ll_length:
            return "The value does not exist."

        current = self.head
        for i in range(self.ll_length - 1, -1, -1):
            if i == k:
                return current.value
            current = current.next


if __name__ == "__main__":
    from node import Node

    ll = LinkedList()
    ll.insert(Node("A"))
    ll.insert(Node("B"))
    ll.insert(Node("C"))
    ll.insert(Node("D"))

    print("------------------- The values in the linked list ---------------")
    print(ll.to_string())
    print(
        "------------------- The values in the linked list after using insert_after method ---------------"
    )
    ll.insert_after("D", Node("JJ"))
    print(ll.to_string())
    print(
        "------------------- The values in the linked list after using insert_before method ---------------"
    )
    ll.insert_before("B", Node("KK"))
    print(ll.to_string())
    print(
        "------------------- The values in the linked list after using the append method ---------------"
    )
    ll.append(Node("append"))
    print(ll.to_string())
    print(
        "------------------- The values in the linked list after using the delete method ---------------"
    )
    ll.delete_node("append")
    print(ll.to_string())
    print(ll.kthFromEnd(2))
    ll.delete_node("KK")
    print(ll.kthFromEnd(2))
