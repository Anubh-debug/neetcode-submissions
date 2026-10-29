class MyHashSet:

    def __init__(self):
        self.list1=set()

    def add(self, key: int) -> None:
        self.list1.add(key)

    def remove(self, key: int) -> None:
        if key in self.list1:
            self.list1.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.list1:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)