class CustomError(Exception):
    pass


class Node:
    """
    A class called Node, which create an object contains two property value and next.
    Input:
        value --> Any
    Output:
        Return object --> {
                        value : any
                        next : None
                    }
    """

    def __init__(self, value):
        self.id = 0
        self.value = value
        self.next = None


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

    def insert(self, value):
        """
        Insert method, take the input and add it after the head.
        Input:
            Node -> Type object
        Output:
            New node in linked list.
        """
        try:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        except AttributeError:
            raise CustomError("Something went wrong with the insertion!")

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
            return
        current = self.head
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
                    break
                except AttributeError:
                    self.head = current_node.next
                    break
            if current_node.next == None:
                print("Not Found")
                break
            prev_node = current_node
            current_node = current_node.next

    def get_ll_length(self):
        """
        This function take no arguments and return the length
        of the linked list.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def kthFromEnd(self, k):
        """
        kthFromEnd method used to get the value of a specific position.

        Input:
            k -> integer, positive number
        Output:
            Return -> The value of that postion if it exist.

        """
        ll_length = self.get_ll_length()
        if k < 0 or type(k) is not int:
            return "Negative numbres or non-integer numbers not acceptable."

        if k >= ll_length:
            return "The value does not exist."

        current = self.head
        for i in range(ll_length - 1, -1, -1):
            if i == k:
                return current.value
            current = current.next

    @staticmethod
    def zip_list(ll_1, ll_2):
        """
        The zip_list function took two objects as an arguments, the zip function linked the two lists together into one so that the nodes alternate between the two lists and return a reference to the  zipped list.

        Input:
            ll_1 -> linked list object
            ll_2 -> linked list object

        Output:
            Return -> the zipped linked list
        """
        current_ll_1 = ll_1.head
        current_ll_2 = ll_2.head

        while current_ll_2:
            if current_ll_1 == None and current_ll_2 != None:
                ll_1.append(current_ll_2)
                break
            ll_1.insert_after(current_ll_1.value, Node(current_ll_2.value))
            current_ll_1 = current_ll_1.next.next
            current_ll_2 = current_ll_2.next
        return ll_1


if __name__ == "__main__":
    from node import Node

    ll = LinkedList()
    ll.insert(Node("E"))
    ll.insert(Node("D"))
    ll.insert(Node("C"))
    ll.insert(Node("B"))
    ll.insert(Node("A"))

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

    ll_2 = LinkedList()
    ll_2.insert(Node(4))
    ll_2.insert(Node(4))
    ll_2.insert(Node(3))
    ll_2.insert(Node(2))
    ll_2.insert(Node(1))

    print(ll_2.to_string())
    print("Linked List length: ", ll_2.get_ll_length())

    zipped_ll = LinkedList.zip_list(ll, ll_2)
    print(zipped_ll.to_string())
    print("Linked List length: ", zipped_ll.get_ll_length())
    print(zipped_ll.kthFromEnd(0))
    zipped_ll.delete_node("KK")
    print(zipped_ll.to_string())
    print(zipped_ll.kthFromEnd(11))
