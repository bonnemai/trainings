from typing import List
# Write any import statements here
# def cost(i1:int, j1: int,i2:int, j2: int, n:int=10):
#     if i1==j1 or i2==j2: 
#       return 0
#     return min(n-abs(i1-j1), abs(j1-i1), n-abs(i2-j2), abs(j2-i2)) 
def cost(i1:int, j1: int, n:int=10):
    if i1==j1 : 
      return 0
    return min(n-abs(i1-j1), abs(j1-i1)) 


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # l1=1
  l2=1
  # Write your code here
  results=cost(1,C[ 0], N)
  l1=C[0]
  for i in range(M-1): 
    c1=cost(l1,C[ i+1], N)
    c2=cost(l2,C[ i+1], N)
    if c1<c2:
      l1=C[i+1]
      results+=c1
    else:
      l2=C[i+1]
      results+=c2
  return results


tests=[
    # (10, 1, [2], 1),
    # (10, 1, [10], 1),
    # (10, 1, [9], 2),
    # (10, 4, [2,3,4,5], 4),
    (3,3,[1,2,3], 2), 
    (10, 4, [9, 4, 4, 8], 6)
]
for (N,M,C,expected_results) in tests:
    res=getMinCodeEntryTime(N,M,C)
    print(res==expected_results, res)
# print(cost(1, 10, 10))
# print(cost(1, 1, 10))
# print(cost(1, 2, 10))