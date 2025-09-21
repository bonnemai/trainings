def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    result = []
    n = len(ranked)
    for score in player:
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if ranked[mid] == score:
                low = mid
                break
            elif ranked[mid] < score:
                high = mid - 1
            else:
                low = mid + 1
        result.append(low + 1)
    return result
ranked=[100 ,100, 50, 40, 40, 20, 10]
players=[5 ,25, 50, 120, 150]

tests=[
    (ranked, players, [6, 4, 2, 1]) 
]
for (ranked, players, exp) in tests:
    res=climbingLeaderboard(ranked, players)
    print (res, exp)