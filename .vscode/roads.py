from typing import List

from collections import deque

def bfsOfGraph(adj, s, visited, res):
    
    # Create a queue for BFS
    q = deque()
    
    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)
    
    # Iterate over the queue
    while q:
        
        # Dequeue a vertex and store it
        curr = q.popleft()
        res.append(curr)
        
        # Get all adjacent vertices of the dequeued 
        # vertex curr If an adjacent has not been 
        # visited, mark it visited and enqueue it
        for x in adj[curr]:
            print(x)
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

# Perform BFS for the entire graph which maybe
# disconnected
def bfsDisconnected(adj):
    V = len(adj)
    
    # create an array to store the traversal
    res = []
    
    # Initially mark all the vertices as not visited
    visited = [False] * V
    
    # perform BFS for each node
    for i in range(V):
        if not visited[i]:
            bfsOfGraph(adj, i, visited, res)
    return res

def to_nodes(N, roads):
    nodes=[[]for _ in range(N)]
    for r in roads:
        nodes[r[0]].append(r[1])
        nodes[r[1]].append(r[0])
    return nodes
    # nodes=[]
    # for r in roads:
    #     nodes.append(r[0])
    #     nodes.append(r[1])
    # return nodes

# if __name__ == "__main__":
#     adj = [[1, 2], [0], [0],
#         [4], [3, 5], [4]]
#     ans = bfsDisconnected(adj)
#     for i in ans:
#         print(i, end=" ")

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        nb_roads_per_city=[]
        for i in range(n):
            nb_roads=0 
            for r in roads:
                if i in r:
                    nb_roads+=1
            nb_roads_per_city.append(nb_roads)
        nb_roads_per_city_copy=nb_roads_per_city.copy()
        _max=max(nb_roads_per_city)
        _max_idx=nb_roads_per_city.index(_max)
        nb_roads_per_city.pop(_max_idx)
        _max2=max(nb_roads_per_city)
        for i in range(n): 
            if _max_idx!=i and nb_roads_per_city_copy[i]==_max2:
                _max2_idx=i
                break
        results=_max+_max2
        print(_max, _max_idx, _max2, _max2_idx, nb_roads_per_city, nb_roads_per_city_copy)
        for r in roads: 
            if (_max_idx ==r[0] and _max2_idx ==r[1])or (_max_idx ==r[1] and _max2_idx ==r[0]): 
                results-=1
        return results

arr=to_nodes(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
print(arr)
res=bfsDisconnected(arr)
print(res)

# solution=Solution()
# tests=[
#     (8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]], 5)
#     ]
# for (n, roads, expected_results) in tests:
#     res=bfsDisconnected(roads)
#     print(res==expected_results, res, expected_results)
    # res=solution.maximalNetworkRank(n, roads)
    # print(res==expected_results, res, expected_results)
# print(solution.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
# print(solution.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
# print(solution.maximalNetworkRank(2, [[1,0]]))