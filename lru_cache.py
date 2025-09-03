from itertools import count
from headq import heappush, heappop
REMOVED = '<removed-task>'      # placeholder for a removed task
        
class LRUCache:
    def __init__(self, capacity: int):
        # self.capacity=capacity
        # self.kv_map={}
        # self.usage_heapq=[]
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = count()     # unique sequence count


    def get(self, key: int) -> int:
        if key in self._map:
            self.usage_map[key]+=1 
            return self._map[key].value
        return -1
    
    def put(self, key: int, value:int):
        'Add a new task or update the priority of an existing task'
        if key in self.entry_finder:
            self.remove_task(key)
        cnt = next(self.counter)
        entry = [ cnt, key, value]
        self.entry_finder[key] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            cnt, key, value = heappop(self.pq)
            if key is not REMOVED:
                del self.entry_finder[key]
                return key
        raise KeyError('pop from an empty priority queue')

        # if self.kv_map.size()<=self.capacity: 



# Your LRUCache object will be instantiated and called as such:
capacity =3
key=1
value=1
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)