if __name__ == "__main__":
    from hash_map import HashTable, Node, CustomError
else:
    from hash_table.hash_map import HashTable, Node


class RepeatedWord(HashTable):
    def _filter_word(self, string):
        if not isinstance(string, str):
            raise CustomError("Invalid input!")

        words = string.split()

        for idx, word in enumerate(words):
            newStr = word.replace(",", "")
            words[idx] = newStr
        return words

    def repeated_word(self, string):
        words = self._filter_word(string)

        for word in words:
            word = word.lower()
            new_node = Node(word, word)
            index = self._hash(word)
            bucket = self.buckets[index]
            if bucket == None:
                self.buckets[index] = new_node
                continue
            prev = None
            while bucket:
                if bucket.value == word:
                    return word
                prev = bucket
                bucket = bucket.next
                prev.next = new_node


if __name__ == "__main__":

    ht = RepeatedWord(10)
    print(ht.repeated_word(""))
