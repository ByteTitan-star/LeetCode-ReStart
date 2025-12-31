# 题目链接：https://leetcode.cn/problems/search-insert-position/description/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

if __name__ == '__main__':
    print(Solution().searchInsert( [1,3,5,6], 5))