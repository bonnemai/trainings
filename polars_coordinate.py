# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
from math import sqrt

# x=input()
def polare(x):
    if '+' in x: 
        x,y=x.split('+')
    elif '-' in x: 
        x_split=x.split('-')
        if len(x_split)==3: # -1-2j
            x='-'+x_split[1]
            y='-'+x_split[2]
        elif len(x_split)==2: # 1-2j
            x=x_split[0]
            y='-'+x_split[1]
            
    x=float(x)
    y=float(y.replace('j', ''))
    res1=sqrt(x**2+y**2)
    res2=abs(phase(complex(x, y)))
    return res1, res2

print(polare('-1-5j'))
