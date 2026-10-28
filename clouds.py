from collections import deque
def get_neighbours(r:int, c:int, max_r:int, max_c:int)->list[tuple[int,int]]: 
    shifts=[(0, 1), (0, -1), (1, 0), (-1, 0)]
    results=[]
    for shift in shifts: 
        r=r+shift[0]
        c=c+shift[1]
        if 0<=r<max_r and 0<=c<max_c: 
            results.append((r, c))
    return results

def bfs(matrix, r, c)-> None: 
    d=deque([(r, c)])
    max_r=len(matrix)
    max_c=len(matrix[0])
    while d: 
        r, c=d.popleft()
        neighbourgs=get_neighbours(r, c, max_r, max_c)
        for r, c in neighbourgs: 
            if matrix[r][c]=='1': 
                matrix[r][c]='0'
                bfs(matrix, r, c)

def get_cloud(matrix: list[list[str]])-> int: 
    nb_clouds=0
    for r in range(len(matrix)): 
        for c in range(len(matrix[0])): 
            if matrix[r][c]=="1":
                matrix[r][c]="0"
                nb_clouds+=1
                bfs(matrix, r, c)
    return nb_clouds


if __name__=="__main__": 
    tests=[
        ([['0', '0', '0', '0'],
          ['0', '1', '1', '0'], 
          ['0', '1', '1', '0'], 
          ['0', '0', '0', '0']], 1),
        ([['1', '0', '0', '0'],
          ['0', '0', '0', '0'], 
          ['0', '0', '0', '0'], 
          ['0', '0', '0', '1']], 2),
        ([['1', '0', '0', '1'],
          ['0', '0', '0', '0'], 
          ['0', '0', '0', '0'], 
          ['0', '0', '0', '1']], 3)
          ]

    for matrix, expected_result in tests: 
        result=get_cloud(matrix)
        assert result==expected_result, f"expected: {expected_result}, got {result} for Matrix {matrix}"