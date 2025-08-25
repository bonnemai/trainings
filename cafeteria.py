from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    """
    Efficient algorithm to find maximum additional diners that can be seated.
    
    Time Complexity: O(M log M) where M is the number of occupied seats
    Space Complexity: O(M)
    """
    if not S:
        # If no seats are occupied, we can seat people at every 2K+1 position
        return (N + 2*K) // (2*K + 1)
    
    # Sort occupied seats for efficient processing
    S.sort()
    
    result = 0
    
    # Check the gap before the first occupied seat
    first_gap = S[0] - 1  # Gap from seat 1 to first occupied seat
    if first_gap > 0:
        # For the first gap, we can seat (first_gap + K) // (K + 1) people
        # because we don't need K empty seats on the left (there are no seats to the left)
        result += (first_gap + K) // (K + 1)
    
    # Check gaps between occupied seats
    for i in range(len(S) - 1):
        gap = S[i + 1] - S[i] - 1  # Gap between two occupied seats
        if gap > 0:
            # In a gap of size g, we can seat g // (2K + 1) people
            # because each person needs K seats on each side
            result += gap // (2*K + 1)
    
    # Check the gap after the last occupied seat
    last_gap = N - S[-1]  # Gap from last occupied seat to seat N
    if last_gap > 0:
        # For the last gap, we can seat last_gap // (K + 1) people
        # because we don't need K empty seats on the right (there are no seats to the right)
        result += last_gap // (K + 1)
    
    return result

# Legacy function for backward compatibility (inefficient version)
# def can_sit(_map, i:int, K:int, N:int):
#     start = max(0, i-K)
#     end = min(N, i+K+1)
#     for j in range(start, end):    
#         if j > 0 and j <= N:
#             if j in _map:
#                 return False
#     return True

# def getMaxAdditionalDinersCount_legacy(N: int, K: int, M: int, S: List[int]) -> int:
#     """Legacy inefficient implementation for comparison"""
#     results = 0
#     _map = {}
#     for seat in S: 
#         _map[seat] = True
#     for i in range(1, N+1):
#         if can_sit(_map, i, K, N):
#             _map[i] = True
#             results += 1
#     return results

if __name__ == '__main__':
    # Test cases
    test_cases = [
        (10, 1, 2, [2, 6]),
        (15, 2, 3, [11, 6, 14]),
        (1000000, 2, 100, [1, 100, 1000, 10000, 100000]),  # Large N test
    ]
    
    for N, K, M, S in test_cases:
        print(f"N={N}, K={K}, M={M}, S={S}")
        result_efficient = getMaxAdditionalDinersCount(N, K, M, S)
        print(f"Efficient result: {result_efficient}")
        
        # Only run legacy version for small N to avoid timeout
        # if N <= 1000:
        #     result_legacy = getMaxAdditionalDinersCount_legacy(N, K, M, S)
        #     print(f"Legacy result: {result_legacy}")
        #     print(f"Results match: {result_efficient == result_legacy}")
        # else:
        #     print("Legacy version skipped for large N (would be too slow)")
        # print("-" * 50)
