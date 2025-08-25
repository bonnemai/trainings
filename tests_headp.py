from heapq import heapify, heappop, heappush, heappushpop, heapreplace

lst=[1,2,3,4,5]
heapify(lst)
# lst=headq(lst)
print(heappop(lst), lst)
print(heappush(lst, 6), lst)
print(heappushpop(lst, 10), lst)
print(heapreplace(lst, 11), lst)

for item in lst:
    print(item)