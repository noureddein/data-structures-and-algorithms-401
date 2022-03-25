# Stacks and Queues
<!-- Short summary or background information -->
  - **Stack**: it is a linear data structure, it consist of nodes, each node pointing to the previous node, and it have an indicator called _top_, the _top_ points to the last node in stack.
  - **Queue**:  it is a linear data structure, it consist of nodes,each node linked to the next node, the queue have two indicators the first one called _front_, the _front_ points to the first node in queue, the second one called _back_ or _rear_, the _back_ points to the last node in queue.

## Challenge
<!-- Description of the challenge -->
 - Implement Stack and Queue class.
 - Implement Stack and Queue methods, 
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