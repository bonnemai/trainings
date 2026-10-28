
from collections import deque
from math import inf


class CountEvents:
    def __init__(self, window: int=5) -> None:
        if window<=0: 
            raise ValueError('Window should be a positive integer. ')
        self.window=window
        self.d=deque()
        self.maximas=deque() # descreasing: the first element is the Max. 
        self.total=0

    def add(self, value:int)->None: 
        self.d.append(value)
        self.total+=value
        
        while self.maximas and self.maximas[-1]<value: 
            self.maximas.pop()
        self.maximas.append(value)
                
        if len(self.d)>self.window: 
            first_value=self.d.popleft()
            self.total-=first_value
            if self.maximas and self.maximas[0]==first_value:
                self.maximas.popleft()
    
    def stats(self)->dict[str, float|int]|None: 
        if self.d: 
            _sorted=sorted(self.d)
            idx=len(self.d)//2
            return {
                'last': self.d[-1], 
                'average': self.total/len(self.d) if len(self.d) else 0, 
                'median': (_sorted[idx-1]+_sorted[idx])/2.0 if len(self.d)%2==0 else  _sorted[idx], 
                'count': len(self.d),
                'maximum' : self.maximas[0] if self.maximas else inf
            }

if __name__=='__main__': 
    ce=CountEvents()
    ce.add(6)
    ce.add(1)
    ce.add(2)
    ce.add(3)
    ce.add(4)
    ce.add(5)
    print(ce.stats())