from stack_and_queue.animal_shelter import AnimalShelter
import pytest


def test_queue_shelter_with_multi_animals(shelter_with_multi_animals):
    actual = shelter_with_multi_animals.print_queue()
    expected = "Front -> { dog } -> { cat } -> { cat } -> { dog } -> { cat } <- Back"
    assert actual == expected


def test_enqueue_to_shelter_with_multi_animals(shelter_with_multi_animals):
    shelter_with_multi_animals.enqueue("Cat")
    actual = shelter_with_multi_animals.print_queue()
    expected = "Front -> { dog } -> { cat } -> { cat } -> { dog } -> { cat } -> { cat } <- Back"
    assert actual == expected


def test_dequeue_the_front(shelter_with_multi_animals):
    shelter_with_multi_animals.dequeue("Dog")
    actual = shelter_with_multi_animals.print_queue()
    expected = "Front -> { cat } -> { cat } -> { dog } -> { cat } <- Back"
    assert actual == expected

    actual = shelter_with_multi_animals.front.value
    expected = "cat"
    assert actual == expected


def test_queue_with_one_animal(shelter_with_one_animal):
    actual = shelter_with_one_animal.print_queue()
    expected = "Front -> { dog } <- Back"
    assert actual == expected


def test_dequeue_from_shelter_with_one_animal(shelter_with_one_animal):
    shelter_with_one_animal.dequeue("Dog")
    actual = shelter_with_one_animal.print_queue()
    expected = "Front ->  <- Back"
    assert actual == expected


def test_dequeue_not_dog_or_cat(shelter_with_multi_animals):
    shelter_with_multi_animals.dequeue("monkey")
    actual = shelter_with_multi_animals.print_queue()
    expected = "Front -> { dog } -> { cat } -> { cat } -> { dog } -> { cat } <- Back"


@pytest.fixture
def shelter_with_multi_animals():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("Dog")
    animal_shelter.enqueue("Cat")
    animal_shelter.enqueue("Cat")
    animal_shelter.enqueue("Dog")
    animal_shelter.enqueue("Cat")

    return animal_shelter


@pytest.fixture
def shelter_with_one_animal():
    shelter = AnimalShelter()
    shelter.enqueue("Dog")
    return shelter
