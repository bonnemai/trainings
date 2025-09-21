def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def extraLongFactorials(n):
    if n == 1:
        print('1')
    if n==2:
        print(2)
    print( range_prod(1,n))

tests=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
for n in tests:
    print (n)
    extraLongFactorials(n)