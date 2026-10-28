
def get_neighbourgs(r:int, c:int, len_r:int, len_c:int)->list[tuple[int,int]]:
    shifts=[(0, 1), (0, -1), (1, 0), (-1, 0)]
    results=[]
    for shift in shifts: 
        new_r=r+shift[0]
        new_c=c+shift[1]
        if 0<=new_r<len_r and 0<=new_c<len_c:
            results.append((new_r, new_c))
    return results
        
def dfs(matrix, r, c): 
    stack=[(r, c)]
    while stack: 
        r, c=stack.pop()
        neighbours=get_neighbourgs(r, c, len(matrix), len(matrix[0]))
        for r, c in neighbours: 
            if matrix[r][c]=='1': 
                stack.append((r , c))
                matrix[r][c]='0'
    

def get_cloud(matrix: list[list[str]])-> int: 
    nb_clouds=0
    for r in range(len(matrix)): 
        for c in range(len(matrix[0])): 
            if matrix[r][c]=="1":
                matrix[r][c]="0"
                nb_clouds+=1
                dfs(matrix, r, c)
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