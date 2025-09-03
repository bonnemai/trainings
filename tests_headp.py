from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest



lst=[(1, 'key1'), (2, 'key2')]
heapify(lst)



# # lst=headq(lst)
# print(heappop(lst), lst)
# print(heappush(lst, 6), lst)
# print(heappushpop(lst, 10), lst)
# print('heapreplace', heapreplace(lst, 11), lst)
print('nlargest', nlargest(2, lst))
# # for item in lst:
# #     print(item)
# for _ in range(len(lst)): 
#     print(heappop(lst))
