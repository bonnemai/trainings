from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  count=0
  for i in range(R):
    for j in range(C):
      count+=G[i][j]
  return 0.0 if R*C==0 else count/(R*C)

if __name__ == '__main__':
    R = 2
    C = 3
    G =[[ 0, 0, 1], [1, 0, 1]]
    print(getHitProbability(R,C,G))