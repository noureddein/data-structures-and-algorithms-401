"""
    ! Task :
        [1] Create a Node class that has properties for the value stored in the Node,
        and a pointer to the next Node.
"""


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
        self.value = value
        self.next = None
