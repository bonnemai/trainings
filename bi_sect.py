from bisect import bisect_left, insort_right, insort, insort_left
a=[1,2,3]
print(bisect_left(a, 2.5))
print(insort_left(a, 2.5))
print(a)