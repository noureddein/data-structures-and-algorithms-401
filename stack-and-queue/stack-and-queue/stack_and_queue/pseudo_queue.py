from stack_and_queue.stack_and_queue import Node


class PseudoQueue:
    def __init__(self, Stack):
        self.stack_alpha = Stack()
        self.stack_holder = Stack()
        self.front = None
        self.back = None

    def enqueue(self, value):
        # Move nodes to stack holder
        while not self.stack_alpha.is_empty():
            self.stack_holder.push(self.stack_alpha.peek())
            self.stack_alpha.pop()

        # Move nodes from stack holder to Queue
        node = Node(value)
        while True:
            if self.front == None:
                self.front = node
                self.back = node
                continue
            if self.stack_holder.is_empty():
                break
            node = Node(self.stack_holder.peek())
            self.stack_holder.pop()
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.front == None:
            return "Queue is empty!"
        temp = self.front
        self.front = self.front.next
        temp.next = None


if __name__ == "__main__":
    from trees.trees.stack_and_queue import Stack, Node

    pseudo_queue = PseudoQueue(Stack)
    pseudo_queue.stack_alpha.push("A")
    pseudo_queue.enqueue(5)
    # pseudo_queue.dequeue()
    print(pseudo_queue.front.next)
