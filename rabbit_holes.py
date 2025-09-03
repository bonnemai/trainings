from typing import List
# Write any import statements here

def pages_visited(L, i): 
  j=i
  visited=[]
  while j not in visited:
    visited.append(j)
    j=L[j]-1
  return len(visited)

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
  visited_array=[]
  _cache={}
  _max=0
  for i in range(N): 
    pv=pages_visited(L,i)
    visited_array.append()

  return max(visited_array)

tests=[
    # (  [4, 1, 2, 1], 4), 
    ([4, 3, 5, 1, 2], 3)
    ]
for ( L, expected_value) in tests:
    res=getMaxVisitableWebpages(len(L), L)
    print(res==expected_value, res)