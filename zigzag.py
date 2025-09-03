def display(matrix: []):
    results = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            results+=matrix[i][j]
    return results

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        print(len(s)//numRows)
        m=len(s)//numRows+1
        n=numRows
        matrix=[['']*m]*n
        for i in range(n): 
            matrix[i]=['']*m
        i=0
        j=0
        for i_char in range(len(s)): 
            if i_char>0 and i_char%numRows==0:  
                i=0
                j+=1
            matrix[i][j]=s[i_char]
            i+=1
        return display(matrix)

txt='PAYPALISHIRING'
tests=[
    (txt, len(txt)-2,'PAYPALISHIGRNI'),
    (txt, len(txt)-1,'PGAYPALISHIRIN'),
    (txt, 100,txt),
    ('A', 1,'A'),
    # ('PAYPALISHIRING', 3,'PAHNAPLSIIGYIR')
    ]
s=Solution()
for (input, numRows, expected_output) in tests:
    results = s.convert(input, numRows)
    print(input, results, expected_output, results==expected_output)