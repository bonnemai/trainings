from typing import List
# Write any import statements here

# def gain(V, C, S, actions, i, start):
#   return (1-S)*V[i]-C
def get_expected_values(V, C, S, i, start):
  results=0
  power=1
  for j in range(start, i): 
    expected_value=V[j]
    results+=expected_value
    # if expected_value>C:÷
    power+=1
  return results


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here
  actions=[False]*N
#   for i in range(N): 
    
  return 0.0

# print(gains([10, 2, 8, 6, 4], 5, 0, 5, 0))
print(get_expected_values([10, 2, 8, 6, 4], 5, 1, 5, 0))