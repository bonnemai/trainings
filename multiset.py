from collections import defaultdict
class MultiSet:
    def __init__(self) -> None:
        self.arr=[]
        self.map=defaultdict(set)

    def __repr__(self) -> str:
        return str(self.arr)

    def add(self, element):
        self.arr.append(element)
        self.map[element].add(len(self.arr)-1)

    def remove(self, element):
        if element in self.map:
            idx=self.map[element].pop()
            last_idx=len(self.arr)-1
            last_val=self.arr[last_idx]
            if idx!=last_idx:
                self.arr[idx]=last_val
                self.map[last_val].add(idx)
                self.map[last_val].discard(last_idx)
            self.arr.pop()
            if not self.map[element]: 
                del self.map[element]

    def get_random(self):
        from random import choice
        if len(self.arr):
            return choice(self.arr)
    
m=MultiSet()
m.add(1)
m.add(1)
print(m)
m.remove(1)
print(m.get_random())
print(m)
m.remove(1)
print(m)
m.remove(1)
print(m)


m=MultiSet()
m.add(1)
m.add(1)
m.add(2)
print(m)
m.remove(1)
print(m.get_random())
print(m)
m.remove(1)
print(m)
m.remove(1)
print(m)
