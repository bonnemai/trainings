from collections import deque


graph={
    "A": ["B", "C"], 
    "B": ["A", "D"], 
    "C": ["A", "D"], 
    "D": ["B", "C", "E"], 
    "E": ["D"]
}
def shortest_path(graph, start="A", end="E"): 
    visited={start}
    d=deque([(start, 0)])
    while d: 
        node, distance=d.popleft()
        for neighbour in graph[node]: 
            if neighbour==end: 
                return distance
            if neighbour not in visited: 
                visited.add(neighbour)
                d.append((neighbour, distance+1))
    return -1

if __name__=="__main__":
    result =shortest_path(graph)  
    assert result ==2, f"Answer is {result}"