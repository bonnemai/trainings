import heapq
from collections import defaultdict
class Volumes:
    def __init__(self):
        self.totals = defaultdict(int)  # ticker -> volume

    def addVolume(self, ticker: str, volume: int):
        """
        O(1)
        """
        self.totals[ticker] += volume

    def get_largest_volume(self, top_n: int):
        """
        O(M log(top_n))
        # returns list[(ticker, volume)] largest first
        """
        return heapq.nlargest(top_n, self.totals.items(), key=lambda kv: kv[1])

v=Volumes()
v.addVolume('A', 100)
v.addVolume('B', 200)
print('get_largest_volume', v.get_largest_volume(2))
v.addVolume('A', 200)
print('get_largest_volume', v.get_largest_volume(1))