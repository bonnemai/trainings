

from collections import deque


points=[100, 102, 101, 105, 104]

class MvAvg: 
    def __init__(self, nb_elements: int=3) -> None:
        self.nb_elements = nb_elements
        self.total=0
        self.d=deque()

    def add_point(self, point:int)-> float: 
        self.d.append(point)
        self.total+=point
        if len(self.d)>self.nb_elements: 
            self.total-=self.d.popleft()
        return self.total/len(self.d)


def get_mv_average(points: list[int], nb_elements:int)-> list[float]: 
    # d=deque()
    mv_avg=MvAvg(nb_elements)
    results = []
    for point in points:
        results.append(mv_avg.add_point(point))
    return results

print(get_mv_average(points, nb_elements=3))