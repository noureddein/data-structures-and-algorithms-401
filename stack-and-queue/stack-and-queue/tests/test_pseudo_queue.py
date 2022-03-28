from stack_and_queue.pseudo_queue import PseudoQueue
from stack_and_queue.stack_and_queue import Stack
import pytest


def test_push_to_stack(pseudo_obj):
    top = pseudo_obj.stack_alpha.peek()
    actual = top
    expected = "C"
    assert actual == expected


def test_enqueue(pseudo_obj):
    pseudo_obj.enqueue(5)
    actual = pseudo_obj.front.value
    expected = 5
    assert actual == expected


def test_second_node_from_queue(pseudo_obj):
    pseudo_obj.enqueue(5)
    actual = pseudo_obj.front.next.value
    expected = 'A'

    assert actual == expected


def test_dequeue(pseudo_obj):
    pseudo_obj.enqueue(5)
    actual = pseudo_obj.front.value
    expected = 5

    assert actual == expected

    pseudo_obj.dequeue()
    actual = pseudo_obj.front.value
    expected = 'A'

    assert actual == expected


def test_dequeue_empty_queue():
    empty_pseudo_queue = PseudoQueue(Stack)
    actual = empty_pseudo_queue.dequeue()
    expected = "Queue is empty!"
    assert actual == expected


@pytest.fixture
def pseudo_obj():
    pseudo_queue = PseudoQueue(Stack)
    pseudo_queue.stack_alpha.push('A')
    pseudo_queue.stack_alpha.push('B')
    pseudo_queue.stack_alpha.push('C')
    return pseudo_queue
