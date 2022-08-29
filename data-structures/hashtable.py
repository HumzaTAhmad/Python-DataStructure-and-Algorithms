
class HashTable:
    def __init__ (self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)
        return h % 10
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


class main: 
    t = HashTable()
    t["march 6"] = 130
    t["march 17"] = 5
    print(t["march 6"])
    print(t["march 17"])
    del t["march 17"]
    print(t.arr)
  
