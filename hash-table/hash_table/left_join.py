from turtle import right


if __name__ == "__main__":
    from hash_map import HashTable, CustomError
    from linked_list import LinkedList
else:
    from hash_table.hash_map import HashTable, CustomError
    from hash_table.linked_list import LinkedList


class JoinTables(HashTable):
    def __init__(self, table_1, table_2, INITIAL_CAPACITY=1024):
        super(JoinTables, self).__init__(INITIAL_CAPACITY)
        if not isinstance(table_1, HashTable) or not isinstance(table_2, HashTable):
            raise CustomError("The tables should be instance of hash-map table!")
        self.table_1 = table_1
        self.table_2 = table_2
        self.table_1_keys = table_1.get_keys()
        self.table_2_keys = table_2.get_keys()
        self.ll = LinkedList()

    def _walk(self, keys_1, keys_2, get_from_table_1, get_from_table_2):
        for key in keys_1:
            if key in keys_2:
                value = [key, get_from_table_1.get(key), get_from_table_2.get(key)]
                self.ll.insert(value)
            else:
                value = [key, get_from_table_1.get(key), None]
                self.ll.insert(value)

    def join(self, join_to="left"):
        if join_to == "left":
            self._walk(self.table_1_keys, self.table_2_keys, self.table_1, self.table_2)
        if join_to == "right":
            self._walk(self.table_2_keys, self.table_1_keys, self.table_2, self.table_1)

        return self.ll


if __name__ == "__main__":
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

    def add_values_to_table(table_values, table):
        for values in table_values:
            table.set(key=values[0], value=values[1])

    add_values_to_table(table_1_values, table_1)
    add_values_to_table(table_2_values, table_2)

    table_join = JoinTables(table_1, table_2, 10)
    ll = table_join.join()
    print(ll.to_string())
