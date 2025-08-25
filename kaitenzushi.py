from typing import List
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    """
    Count the maximum number of dishes that can be eaten.
    
    Rules:
    - Eat a dish if it's not the same type as any of the previous K dishes eaten
    - Maintain order of dishes eaten
    - Use a sliding window to track the last K dishes eaten
    
    Optimized version using set for O(1) lookup
    """
    if K == 0:
        return N  # Can eat all dishes if K=0
    
    eaten_dishes = deque()  # Sliding window of last K dishes eaten (for order)
    eaten_types = set()     # Set of dish types in the last K dishes (for O(1) lookup)
    count = 0
    
    for i in range(N):
        current_dish = D[i]
        
        # O(1) check if current dish type is already in the last K dishes eaten
        if current_dish not in eaten_types:
            # Eat the dish
            count += 1
            eaten_dishes.append(current_dish)
            eaten_types.add(current_dish)
            
            # Remove oldest dish if we have more than K dishes
            if len(eaten_dishes) > K:
                oldest_dish = eaten_dishes.popleft()
                eaten_types.remove(oldest_dish)
    
    return count

if __name__=='__main__': 
    tests=[
        ([1,2,3,3,2,1], 1, 5), 
        ([1,2,3,3,2,1], 2, 4),
        ([1,2,1,2,1,2,1], 2, 2),
        ([1,1,1,1,1,1,1,1,1], 2, 1),
        ([1,2,3,4,5,6,7,8], 2, 8),
        ([1,2,3,4,5,6,7,8], 1, 8),
        ([1,2,3,4,5,6,7,8], 8, 8),
        ([1,1,2,2,3,3,4,4], 1, 4),
        ([1,1,2,2,3,3,4,4], 2, 4),
        ([1,1,2,2,3,3,4,4], 3, 4),
        ([1,1,2,2,3,3,4,4], 4, 4)
    ]
    
    for D, K, expected in tests: 
        result = getMaximumEatenDishCount(len(D), D, K)
        status = "✓" if result == expected else "✗"
        print(f'{status} D={D}, K={K}: got {result}, expected {expected}')