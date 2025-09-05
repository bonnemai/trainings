from collections import deque

def bfs(graph): 
    visited=[False]*len(graph)
    stack=deque([graph[0]])
    while stack: 
        nodes=stack.popleft()
        for node in nodes:
            if not visited[node]: 
                visited[node]=True
                stack.append(graph[node])
                print (node)

test1=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
bfs(test1)