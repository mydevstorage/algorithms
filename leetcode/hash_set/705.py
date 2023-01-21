'''Design HashSet'''

 # A prime number

class MyHashSet:

    def __init__(self):
       
        self.key_space = 2069
        self.hash_table = [[] for _ in range(self.key_space)]

    def add(self, key: int) -> None:
        mod = key % self.key_space
        if not key in self.hash_table[mod]:
            self.hash_table[mod].append(key)

    def remove(self, key: int) -> None:
        mod = key % self.key_space
        # Remove if it's present
        try:
            self.hash_table[mod].remove(key)
        except:
            pass
           
    def contains(self, key: int) -> bool:
        mod = key % self.key_space
        return key in self.hash_table[mod]

a = MyHashSet()
a.add(1)
a.add(2)
a.add(2)
print(a.contains(2))
a.remove(2)
print(a)