from collections import defaultdict

def dfs_rec(adjascency, visited, s, rec): 
    visited[s]=True
    for i in adjascency[s]: 
        if not visited[i]: 
            rec.append(i)
            dfs_rec(adjascency, visited, i, rec)

def dfs(adjacency): 
    visited=[False]*len(adjacency)
    rec=[]
    for i in range(len(adjacency)):
        if not visited[i]:
            dfs_rec(adjacency, visited, i, rec)
    return rec

edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
adj=defaultdict(list)
for e in edges: 
    adj[e[0]].append(e[1])
    adj[e[1]].append(e[0])

# adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

rec=dfs(adj)
print(rec)