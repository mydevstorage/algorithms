'''Design HashMap'''

class MyHashMap:
    def __init__(self):
        self.key_space = 2069
        self.hash_table = [[] for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self. key_spacehas
        found = False
        for i, kv in enumerate(self.hash_table[hash_key]):
            if key == kv[0]:
                self.hash_table[hash_key][i] = (key, value)
                found = True
                break
        if not found:
            self.hash_table[hash_key].append((key,value))      

    def get(self, key: int) -> int:
        hash_key = key % self. key_space
        for (k,v) in self.hash_table[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        for i,kv in enumerate(self.hash_table[hash_key]):
            if key == kv[0]:
                del self. hash_table[hash_key][i]

a = MyHashMap()
a.put(1, 2)
a.put(3, 6)
a.put(5, 'ewe')

print(a.get(5))   
# a.remove(5)
print(a.get(5))  
