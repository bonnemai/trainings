

from collections import deque


class TimeEvents:
    def __init__(self, time_window: int=5) -> None:
        if time_window<=0: 
            raise ValueError('Window should be a positive integer. ')
        self.time_window=time_window
        self.values=deque()
        self.maximas=deque()
        self.total=0

    def add(self, timestamp: int, value:int)->None: 
        self.values.append((timestamp, value))
        self.total+=value
        while self.values and self.values[0][0]<timestamp-self.time_window: 
            first_value=self.values.popleft()
            self.total-=first_value[1]
            if self.maximas and first_value==self.maximas[0]: 
                self.maximas.popleft()
        while self.maximas and self.maximas[-1][1]<value: 
            self.maximas.pop()
        self.maximas.append((timestamp, value))
    
    def stats(self)->dict[str, float|int]|None: 
        if self.values: 
            _sorted=sorted(v for _, v in self.values)
            idx=len(self.values)//2
            return {
                'last': self.values[-1][1], 
                'average': self.total/len(self.values), 
                'median': (_sorted[idx-1]+_sorted[idx])/2.0 if len(self.values)%2==0 else  _sorted[idx], 
                'count': len(self.values),
                'maximum' : self.maximas[0][1]
            }

if __name__=='__main__': 
    ce=TimeEvents()
    ce.add(1, 6)
    ce.add(2, 1)
    ce.add(3, 2)
    ce.add(4, 3)
    ce.add(5, 4)
    ce.add(6, 5)
    print(ce.stats())