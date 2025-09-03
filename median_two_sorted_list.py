from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2)==0:
            return 0
        if len(nums1)==0 and len(nums2)>0:
            return nums2[len(nums2)//2]
        if len(nums1>0 and len(nums2)==0:
            return nums1[len(nums1)//2]

        total_n=len(nums1)+len(nums2)
        median=nums1[0]
        median_idx=0
        idx_1=0 #len(nums1)//2
        idx_2=0 #len(nums2)//2

        for i in range(total_n)


        # if (len(nums1)+len(nums2))%2==0:
        #     total_n=len(nums1)+len(nums2)
        #     idx_1=0 #len(nums1)//2
        #     idx_2=0 #len(nums2)//2

        #     median=nums[idx_1]
        #     while (idx_1+idx_2)!=total_n/2: 
        #         if nums1[idx_1+1]<nums2[idx_2+1]:
        #             idx_1+=1
        #         else:
        #             idx_2+=1
            
        # median=nums1[idx]
        # for i in range(len(nums1): 
