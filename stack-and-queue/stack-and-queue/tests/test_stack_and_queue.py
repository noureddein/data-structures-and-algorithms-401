from cmath import exp
from stack_and_queue.stack_and_queue import Stack, Queue
import pytest


# ________________________________
# ========= Testing Stack ========


def test_top_of_stack(stack):
    """Can successfully push onto a stack"""
    actual = stack.top.value
    expected = "C"

    assert actual == expected


def test_push_multiple_values(stack):
    """Can successfully push multiple values onto a stack"""
    actual = stack.top.value
    expected = 'C'
    assert actual == expected

    stack.push('D')
    actual = stack.top.value
    expected = 'D'
    assert actual == expected


def test_pop_node(stack):
    """Can successfully pop off the stack"""
    actual = stack.top.value
    expected = 'C'
    assert actual == expected

    stack.pop()
    actual = stack.top.value
    expected = 'B'

    assert actual == expected


def test_empty_stack_after_multiple_pops(stack):
    """Can successfully empty a stack after multiple pops"""
    stack.pop()
    stack.pop()
    stack.pop()

    actual = stack.top
    expected = None
    assert actual == expected


def test_peek(stack):
    stack.push('John')
    actual = stack.top.value
    expected = 'John'

    assert actual == expected


def test_peek_the_next_item(stack):
    """Can successfully peek the next item on the stack"""
    peek = stack.peek()
    actual = peek
    expected = 'C'
    assert actual == expected

    actual = stack.top.next.value
    expected = 'B'
    assert actual == expected

    actual = stack.top.next.next.value
    expected = 'A'
    assert actual == expected


def test_not_empty_stack(stack):
    actual = stack.is_empty()
    expected = False

    assert actual == expected


def test_empty_stack():
    """Can successfully instantiate an empty stack"""
    empty_stack = Stack()
    actual = empty_stack.is_empty()
    expected = True
    assert actual == expected


def test_empty_stack_raises_exception():
    """Calling pop or peek on empty stack raises exception"""
    stack = Stack()

    pop_empty_stack = stack.pop()
    actual = pop_empty_stack
    expected = "Stack empty"
    assert actual == expected

    call_empty_peek_stack = stack.peek()
    actual = call_empty_peek_stack
    expected = "Stack empty"
    assert actual == expected


# ________________________________
# ========= Testing Queue ========


def test_enqueue_into_queue(queue):
    """Can successfully enqueue into a queue"""
    last_value = queue.back.value
    actual = last_value
    expected = 'Jonathan'
    assert actual == expected

    queue.enqueue('Sonia')
    last_value = queue.back.value
    actual = last_value
    expected = 'Sonia'
    assert actual == expected


def test_enqueue_multiple_values():
    """Can successfully enqueue multiple values into a queue"""
    queue_numbers = Queue()
    queue_numbers.enqueue(1)
    front = queue_numbers.front.value
    back = queue_numbers.back.value

    actual_front = front
    actual_back = back
    expected_front = 1
    expected_back = 1
    assert actual_front == expected_front and actual_back == expected_back

    queue_numbers.enqueue(2)
    front = queue_numbers.front.value
    back = queue_numbers.back.value

    actual_front = front
    actual_back = back
    expected_front = 1
    expected_back = 2
    assert actual_front == expected_front and actual_back == expected_back

    queue_numbers.enqueue(3)
    front = queue_numbers.front.value
    back = queue_numbers.back.value

    actual_front = front
    actual_back = back
    expected_front = 1
    expected_back = 3
    assert actual_front == expected_front and actual_back == expected_back


def test_dequeue_expected_value(queue):
    """Can successfully dequeue out of a queue the expected value"""
    front = queue.peek()
    actual = front
    expected = 'John'
    assert actual == expected

    queue.dequeue()
    front = queue.peek()
    actual = front
    expected = 'Mike'
    assert actual == expected


def test_peek(queue):
    """Can successfully peek into a queue, seeing the expected value"""
    front = queue.front.value
    actual = front
    expected = 'John'
    assert actual == expected


def test_empty_queue_after_multiple_dequeues(queue):
    """Can successfully empty a queue after multiple dequeues"""
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    front = queue.front
    actual = front
    expected = None
    assert actual == expected


def test_instantiate_an_empty_queue():
    """Can successfully instantiate an empty queue"""
    empty_queue = Queue()
    actual_front = empty_queue.front
    actual_back = empty_queue.back
    expected = None

    assert expected == actual_front and expected == actual_back


def test_calling_dequeue_peek_on_empty_queue():
    """Calling dequeue or peek on empty queue raises exception"""
    empty_queue = Queue()

    actual_for_dequeue = empty_queue.dequeue()
    expected_for_dequeue = 'Queue empty!'
    assert actual_for_dequeue == expected_for_dequeue

    actual_for_peek = empty_queue.peek()
    expected_for_peek = 'Queue empty!'
    assert actual_for_peek == expected_for_peek


@pytest.fixture
def stack():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    return stack


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue('John')
    queue.enqueue('Mike')
    queue.enqueue('Mary')
    queue.enqueue('Jonathan')
    return queue
