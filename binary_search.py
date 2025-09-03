
def has_value(nums, target): 
    # mid=len(nums)//2
    i_low, i_high=0, len(nums)
    while i_low<i_high: 
        mid=(i_low+i_high)//2
        if nums[mid]==target:
            return True
        elif nums[mid]<target:
            i_low=mid
        else:
            i_high=mid
    return False

nums=[1,2,3,4,5,6,7,8,9,10]
target=7
print(has_value(nums, target))