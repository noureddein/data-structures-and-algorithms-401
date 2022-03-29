from node import Node
from linked_list import LinkedList


"""
    ?[1] Write a function called zip lists
    ?[2] Arguments: 2 linked lists
    ?[3] Return: New Linked List, zipped as noted below
    [4] Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
    [5] Try and keep additional space down to O(1)
    [6] You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

"""


def zip_list(ll_1, ll_2):
    current_ll_1 = ll_1.head  # Value: A
    current_ll_2 = ll_2.head  # Value: 1

    print(ll_1.to_string())
    print(ll_2.to_string())

    while current_ll_2:
        if current_ll_1 == None and current_ll_2 != None:
            ll_1.append(current_ll_2)
            break
        ll_1.insert_after(current_ll_1.value, Node(current_ll_2.value))
        current_ll_1 = current_ll_1.next.next  # Value: B
        current_ll_2 = current_ll_2.next  # Value: 2

    return ll_1  # New linked list


ll_1 = LinkedList()
ll_1.insert(Node("D"))
# ll_1.insert(Node("C"))
# ll_1.insert(Node("B"))
# ll_1.insert(Node("A"))

ll_2 = LinkedList()
ll_2.insert(Node(5))
ll_2.insert(Node(4))
ll_2.insert(Node(3))
ll_2.insert(Node(2))
ll_2.insert(Node(1))

zip_list(ll_1, ll_2)
print(ll_1.to_string())
# print(ll_1.includes("D"))
