# 题目链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
from typing import List
class Solution:
    def findIndex(self,nums:List[int],n:int,target:int) -> int:
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = self.findIndex(nums,n,target)
        if start==n or nums[start] != target: return [-1,-1]
        end = self.findIndex(nums,n,target+1)-1
        return [start,end]

if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))