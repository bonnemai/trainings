from typing import List

def get_nb_walls(walls, start, end): 
    # can be improved later
    nb_walls=0
    for i in walls: 
        if start<=i<=end:
            nb_walls+=1
    return nb_walls
    
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        max_nb_walls=0
        nb_robots=len(robots)
        i=0
        # for i in range(len(robots)): 
        while i<nb_robots: 
            walls_left=get_nb_walls(walls, robots[i]-distance[i], robots[i])
            walls_right=get_nb_walls(walls, robots[i],distance[i]+ robots[i])
            # if walls_right>walls_left:

            # nb_walls=max(walls_left, walls_right)
            # max_nb_walls+=nb_walls
            if walls_right>walls_left:
                robots.pop(i)
                distance.pop(i)
                nb_robots-=1
            i+=1 
            # kill other robots -> Right
        return max_nb_walls

tests=[
    ([63,56,40,45,4,9,44,69,55,26,73,15,12,60,43,39,37,74,36,34,13,23,66,14,11,42,72,3,57,10,53,8,70,17,58,61,30,32], 
    [8,7,4,8,9,5,2,4,5,2,6,9,5,9,5,3,7,6,9,2,8,7,4,3,5,1,7,5,1,3,5,3,5,4,8,7,6,4], 
    [6,22,50,52,20,9,23,75,26,21,60,58,41,28,30], 
    15)
    # ([10,2],   [5,1],   [5,2,7], 3)
    ]
for (robots, distance, walls, expected_results) in tests:
    res=Solution().maxWalls(robots, distance, walls)
    print(res==expected_results, res, expected_results)