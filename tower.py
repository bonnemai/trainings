# Design a class that supports the following operations efficiently for a stream of stock prices:
#   add_price(current_time: int, price: int): Add a stock price at a given timestamp (in seconds).
#   get_min(current_time: int, last_n_seconds: int) -> int: Return the minimum stock price within the last n seconds from the current time. If no price exists in the range, return None.
# The current time is monotonically increasing.

class StockPriceTracker: 
    def __init__(self): 
        self.prices=[]
        # self.min_prices=[]

        
    def add_price(self, current_time: int, price: int)->None: 
        self.prices.append((current_time, price))
        # self.prices.append((current_time, min(price))
        
    
    def get_min(self, current_time: int, last_n_seconds:int)->int|None: 
        """
        " O(n)
        """
        # filtered_prices=list(filter(lambda x: current_time-last_n_seconds<=x[0]<=current_time, self.prices))
        # if len(filtered_prices)>0: 
        #     return min(map(lambda x:x[1], filtered_prices))
        left=current_time-last_n_seconds
        right=current_time
        _time=float('inf')
        while left<right:
            mid=(left+right)//2
            if self.prices[left] is not None and self.prices[left][0]<self.prices[mid][0]:
                right=mid
            elif self.prices[mid] is not None and self.prices[mid][0]<self.prices[right][0]:
                left=mid
            else:
                left+=1
        sub_array=self.prices[mid:]
        sub_array_prices=map(lambda x:x[1], sub_array)
        return min(sub_array_prices)            
        
# test
tracker = StockPriceTracker()

tracker.add_price(100, 10)
tracker.add_price(101, 15)
assert tracker.get_min(102, 1) == 15
assert tracker.get_min(102, 2) == 10

tracker.add_price(103, 11)
tracker.add_price(104, 16)
assert tracker.get_min(105, 1) == 16
assert tracker.get_min(105, 2) == 11
assert tracker.get_min(105, 3) == 11
assert tracker.get_min(105, 5) == 10

# [10, 11, 16]


tracker.add_price(106, 5)
assert tracker.get_min(107, 1) == 5
assert tracker.get_min(107, 2) == 5
assert tracker.get_min(107, 10) == 5
