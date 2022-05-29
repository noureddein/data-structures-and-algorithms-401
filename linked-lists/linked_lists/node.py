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
