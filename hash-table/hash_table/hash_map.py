class CustomError(Exception):
    pass


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"Key: {self.key}, Value: {self.value}"


class HashTable(object):
    def __init__(self, INITIAL_CAPACITY=1024):
        self.hash_table_capacity = INITIAL_CAPACITY
        self.buckets = [None] * self.hash_table_capacity
        self.keys = []

    def _hash(self, key):
        hash_sum = 0
        for idx, char in enumerate(key):
            # hash_sum += (idx+len(char))**ord(char)
            hash_sum += idx + len(key) + ord(char)
        hash = (hash_sum * 19) % self.hash_table_capacity
        return hash

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise CustomError("You entered invalid key")

    def set(self, key, value):
        self._validate_key(key)
        self.keys.append(key)
        idx = self._hash(key)
        node = self.buckets[idx]
        if node is None:
            self.buckets[idx] = Node(key, value)
            return

        while node.next != None:
            node = node.next
        node.next = Node(key, value)

    def get(self, key):
        self._validate_key(key)
        idx = self._hash(key)
        node = self.buckets[idx]
        current = node
        while current is not None and current.key != key:
            current = current.next

        if current:
            return current.value

    def contains(self, key):
        self._validate_key(key)
        is_exist = self.get(key)
        if is_exist:
            return True
        return False

    def get_keys(self):
        if not len(self.keys):
            return "Hash table empty"

        return self.keys

    def __str__(self):
        keys = self.get_keys()
        return ", ".join(keys)


if __name__ == "__main__":
    ht = HashTable(10)
    ht.set("Cat 1", "Milo")
    ht.set("Cat 2", "Olive")
    print(ht.get_keys())
