from hash_table.hashmap_repeated_word import RepeatedWord, HashTable
import pytest


def test_expected_outcome_string_1():
    hashmap = RepeatedWord(10)
    string = "Once upon a time, there was a brave princess who..."

    actual = hashmap.repeated_word(string)
    expected = "a"
    assert actual == expected


def test_expected_outcome_string_2():
    hashmap = RepeatedWord(10)
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

    actual = hashmap.repeated_word(string)
    expected = "it"
    assert actual == expected


def test_expected_outcome_string_3():
    hashmap = RepeatedWord(10)
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    actual = hashmap.repeated_word(string)
    expected = "summer"
    assert actual == expected


def test_expected_failure_1():
    hashmap = RepeatedWord(10)
    with pytest.raises(Exception):
        hashmap.repeated_word(1)


def test_expected_failure_2():
    hashmap = RepeatedWord(10)
    with pytest.raises(Exception):
        hashmap._filter_word(1)
