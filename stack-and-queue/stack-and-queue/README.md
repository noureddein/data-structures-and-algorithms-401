
# **CC 10**: Stacks and Queues
<!-- Short summary or background information -->
  - **Stack**: it is a linear data structure, it consist of nodes, each node pointing to the previous node, and it have an indicator called _top_, the _top_ points to the last node in stack.
  - **Queue**:  it is a linear data structure, it consist of nodes,each node linked to the next node, the queue have two indicators the first one called _front_, the _front_ points to the first node in queue, the second one called _back_ or _rear_, the _back_ points to the last node in queue.

## Challenge
<!-- Description of the challenge -->
 - Implement Stack and Queue class.
 - Implement Stack and Queue methods.
   - Add
   - Delete
   - Peek
   - Is_Empty
 - Test each method

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
  - Efficiency
    - Big-O(1) for space and time complexity.

## API
<!-- Description of each method publicly available to your Stack and Queue-->
  - Stack Methods:
    - **Push**: Add a new node to the stack.
    - **Pop**: Delete last node in stack.
    - **Peek**: Return the value that the top indicates.
    - **is_empty**: Check if the stack empty and return boolean value.
  - Queue Methods:
    - **Enqueue**: Add a new node the the queue.
    - **Dequeue**: Delete the first node from the queue.
    - **Peek**: Return the value of the front node.
    - **is_empty**: Check if the stack empty and return boolean value.

---

# **CC 11**: Pseudo Queue.

## Challenge Summary
<!-- Description of the challenge -->
  - Implement PseudoQueue class.
  - Implement enqueue method that take a value and add new nodes to the queue.
    -  Use stack class to add the items to the queue.
    -  e.g. `[10]->[15]->[20]` -> `[new node]->[10]->[15]->[20]`
 -  Implement dequeue method to delete a node from queue.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Class and enqueue](../whiteboard/class_enqueue.png)
![dequeue](../whiteboard/dequeue_method.png)

## Approach & Efficiency
 - Create a class PseudoQueue with two methods enqueue and dequeue.
   - **Enqueue**: Take a value and looping through a stack to move nodes to another stack to reverse order of the stack. Then with another loop to loop through the second stack, add the new node to queue and then add the elements from the second stack to queue. this method take a Big-O(n) for time and space.
   - **Dequeue**: Take no value and delete first node every time from the queue. This method take a Big-O(1) for time an space.

## Solution
<!-- Show how to run your code, and examples of it in action -->
  - Go to the directory `stack_and_queue` from you terminal.
  - Type `Python` and the file name `stack_and_queue.py` to run the file.

---
# **CC 12**: Animal Shelter.

## Challenge Summary
<!-- Description of the challenge -->
  - Implement a class called **AnimalShelter**
  - Implement a method called **enqueue** to add the animals to the shelter.
  - Implement a method called **dequeue** to to delete animal from queue even if it not at the front. 

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Enqueue and class implementation](./whiteboard/../../whiteboard/enqueue_animals.png)
![Dequeue implementation](./whiteboard/../../whiteboard/dequeue_animal.png)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
  - Create a class AnimalShelter with two methods enqueue and dequeue.
   - **Enqueue**: Take a value of `dog` or `cat` and add it to queue, if the value NOT `dog` or `cat` it do nothing. The efficiency for this method is Big-O(1) for time and space.
   - **Dequeue**: Take a value of `dog` or `cat` and loop through the queue to search for this animal, and delete the first appearance of this animal and return the value of the node that hold the animal.If the user entered an animal that does not exist, it delete the first value of the queue. The efficiency for this method is Big-O(n) for time and Big-O(1) for space.

## Solution
<!-- Show how to run your code, and examples of it in action -->
  - Go to the directory `stack_and_queue` from you terminal.
  - Type `Python` and the file name `stack_and_queue.py` to run the file.


--- 

# **CC 13**: Validate Brackets.

## Challenge Summary
<!-- Description of the challenge -->
  - Write a function called validate brackets, which take string argument and return a boolean if the brackets are balanced.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![validate bracket](../whiteboard/validate_bracket.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
  - Create a function called **validate_brackets** and with a Stack and helper function called **get_closed_function**.
    - The **validate_brackets** function have a loop to loop through the brackets string, if the string have an open bracket I push it to the stack and invoke the helper function which will return a closed bracket then keep looping. if the string have a closed bracket I pop it from stack. After the loop end, I check if the stack empty, the function return _True_, if not it return _False_.

## Solution
<!-- Show how to run your code, and examples of it in action -->
  - Go to the directory `stack_and_queue` from you terminal.
  - Type `Python` and the file name `validate_bracket.py` to run the file.