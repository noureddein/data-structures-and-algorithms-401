from hash_table.left_join import JoinTables, HashTable
import pytest


def test_expected_right_join(tables):
    table_1, table_2 = tables
    right_join = JoinTables(table_1, table_2, 10)
    right_join.join(join_to="right")

    actual = right_join.ll.to_string()
    expected = "{ ['wrath', 'delight', 'anger'] } -> { ['flow', 'jam', None] } -> { ['guide', 'follow', 'usher'] } -> { ['fond', 'averse', 'enamored'] } -> { ['diligent', 'idle', 'employed'] } -> Null"

    assert actual == expected


def test_edge_case():
    with pytest.raises(Exception):
        right_join = JoinTables("", "table_2", 10)
        right_join.join(join_to="right")


def test_expected_left_join(tables):
    table_1, table_2 = tables
    left_join = JoinTables(table_1, table_2, 10)
    left_join.join(join_to="left")

    actual = left_join.ll.to_string()
    expected = "{ ['wrath', 'anger', 'delight'] } -> { ['outfit', 'garb', None] } -> { ['guide', 'usher', 'follow'] } -> { ['fond', 'enamored', 'averse'] } -> { ['diligent', 'employed', 'idle'] } -> Null"

    assert actual == expected


# ===========================
# ==        Helpers        ==
# ===========================
def add_values_to_table(table_values, table):
    for values in table_values:
        table.set(key=values[0], value=values[1])


@pytest.fixture
def tables():
    table_1 = HashTable(10)
    table_1_values = (
        ("diligent", "employed"),
        ("fond", "enamored"),
        ("guide", "usher"),
        ("outfit", "garb"),
        ("wrath", "anger"),
    )
    table_2 = HashTable(10)
    table_2_values = (
        ("diligent", "idle"),
        ("fond", "averse"),
        ("guide", "follow"),
        ("flow", "jam"),
        ("wrath", "delight"),
    )
    add_values_to_table(table_1_values, table_1)
    add_values_to_table(table_2_values, table_2)

    return table_1, table_2
