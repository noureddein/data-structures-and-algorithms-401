from hash_table.hash_table import HashTable
import pytest


def test_set_value(add_values):
    # [1] Setting a key/value to your hashtable results in the value being in the data structure
    actual = add_values.contains('HR Dep.')
    expected = True
    assert actual == expected

    actual = add_values.contains('Reception')
    expected = True
    assert actual == expected


def test_existing_value(add_values):
    # [2] Retrieving based on a key returns the value stored
    actual = add_values.get('HR Dep.')
    expected = ('06-542333', '06-332233')
    assert actual == expected

    actual = add_values.get('Reception')
    expected = ('06-542322', '06-453221')
    assert actual == expected


def test_not_exist_value(add_values):
    # [3] Successfully returns null for a key that does not exist in the hashtable
    actual = add_values.get('Finance Dep.')
    expected = None
    assert actual == expected


def test_keys(add_values):
    # [4] Successfully returns a list of all unique keys that exist in the hashtable
    actual = add_values.keys()
    actual.sort()
    expected = ['Reception', 'Store Dep.', 'HR Dep.', 'account']
    expected.sort()
    assert actual == expected


def test_no_keys(no_keys):
    # [4] Successfully returns a list of all unique keys that exist in the hashtable
    actual = no_keys.keys()
    expected = 'Hash table empty'
    assert actual == expected


def test_collision(collision):
    # [5] Successfully handle a collision within the hashtable
    actual = collision.get('cat')
    expected = {"name": "Milo"}
    assert actual == expected

    actual = collision.contains('tac')
    expected = True
    assert actual == expected


def test_return_value_from_collision(collision):
    # [6] Successfully retrieve a value from a bucket within the hashtable that has a collision
    actual = collision.get('cat')
    expected = {"name": "Milo"}
    assert actual == expected

    actual = collision.get('tac')
    expected = 'tac tac'
    assert actual == expected


def test_hash_key():
    # [7] Successfully hash a key to an in-range value
    ht = HashTable(100)
    expected = True
    hash = ht._hash('test')
    if isinstance(hash, int):
        actual = True
        assert actual == expected
        return
    actual = False
    assert expected == actual


@pytest.fixture
def add_values():
    ht = HashTable(100)
    ht.set('HR Dep.',   ('06-542333', '06-332233'))
    ht.set('Reception', ('06-542322', '06-453221'))
    ht.set('Store Dep.', ('06-112230', '06-443386', '079-1122334'))
    ht.set('account', '079900000')
    return ht


@pytest.fixture
def no_keys():
    ht = HashTable(100)
    return ht


@pytest.fixture
def collision():
    ht = HashTable(100)
    ht.set('cat', {"name": "Milo"})
    ht.set('tac', 'tac tac')
    return ht
