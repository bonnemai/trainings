import heapq
from math import inf
def dijkstra(graph_weighted, start="A")-> dict[str, int|float]:
    distances={node: 0 if node == start else inf for node in graph_weighted.keys()}
    heap=[(0, start)]
    
    while heap: 
        distance, node = heapq.heappop(heap)
        if distance>distances[node]: 
            continue
        
        for neighbourg, neighbourg_distance in graph_weighted[node]: 
            new_distance=distance+neighbourg_distance
            if new_distance<distances[neighbourg]: 
                heapq.heappush(heap, (new_distance, neighbourg))
                distances[neighbourg]=new_distance
    return distances
    
    
graph_weighted = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": []
}

print(dijkstra(graph_weighted, "A"))
# {'A': 0, 'B': 3, 'C': 1, 'D': 4}