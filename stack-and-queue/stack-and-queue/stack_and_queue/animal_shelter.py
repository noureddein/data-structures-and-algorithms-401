from stack_and_queue.stack_and_queue import Node


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, animal):
        if animal.lower() == "cat" or animal.lower() == "dog":
            node = Node(animal.lower())

            if self.front == None:
                self.front = node
                self.back = node

            self.back.next = node
            self.back = node

    def dequeue(self, pref):
        if pref.lower() != "cat" and pref.lower() != "dog":
            return self.dequeue(self.front.value)

        current = self.front
        prev = None
        while current:
            if current.value == pref.lower():
                temp = current

                if self.front == self.back:
                    self.front = None
                    self.back = None
                    return temp.value

                try:
                    prev.next = current.next
                except AttributeError:
                    self.front = self.front.next
                temp.next = None
                return temp.value
            prev = current
            current = current.next

    def print_queue(self):
        current = self.front
        output = "Front -> "
        while current:
            if current == self.back:
                output += "{{ {0} }}".format(current.value)
                break
            output += "{{ {0} }} -> ".format(current.value)
            current = current.next
        output += " <- Back"
        return output


if __name__ == "__main__":
    from stack_and_queue import Node

    shelter = AnimalShelter()
    shelter.enqueue("Dog")
    shelter.enqueue("Cat")
    shelter.enqueue("Cat")
    shelter.enqueue("Dog")
    shelter.enqueue("Cat")

    print(shelter.print_queue())
    print(shelter.dequeue("dogs"))
    print(shelter.print_queue(), "\n")

    # print(shelter.dequeue("cat"))
    # print(shelter.print_queue(), "\n")
