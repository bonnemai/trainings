
from collections import deque


class SimpleWindow: 
    def __init__(self, window:int=5) -> None:
        if window<0: 
            raise Exception("Window can only be positive. ")
        self.window=window
        self.d=deque()
        self.total=0
    
    def add(self, timestamp: int, value: float)-> float: 
        self.d.append((timestamp, value))
        if len(self.d)>self.window: 
            self.total-= self.d.pop()[1]
        self.total+=value
        if len(self.d): 
            return self.total/len(self.d)
        return 0
    

class SimpleTimeWindow: 
    def __init__(self, window:int=5) -> None:
        if window<0: 
            raise Exception("Window can only be positive. ")
        self.window=window
        self.events=[]
        # self.total=0
    
    def add(self, timestamp: int, value: float)-> float: 
        self.events.append((timestamp, value))
        self.events=[e for e in self.events if e[0]>timestamp-self.window]
        return sum(e[1] for e in self.events)/len(self.events)

if __name__=='__main__':
    s=SimpleTimeWindow()
    print(f"{s.add(1, 100)}")
    print(f"{s.add(2, 105)}")
    print(f"{s.add(3, 110)}")
    print(f"{s.add(4, 90)}")
    print(f"{s.add(5, 95)}")
    print(f"{s.add(6, 95)}")
        