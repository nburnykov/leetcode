###########################################################################################
# leetcode problem  https://leetcode.com/problems/design-hashmap/
###########################################################################################

class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        if key > len(self.data) - 1:
            self.data.extend([-1] * (key - len(self.data) + 1))
        self.data[key] = value

    def get(self, key: int) -> int:
        if key > len(self.data) - 1:
            return -1
        return self.data[key]

    def remove(self, key: int) -> None:
        if key < len(self.data):
            self.data[key] = -1