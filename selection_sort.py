
l=[4,3,2,1]
for i in range(len(l)): 
    # l[0]=min(l)-min
    _min=min(l[i:len(l)])
    idx=l.index(_min)
    l[i], l[idx]=_min, l[i]
print(l)