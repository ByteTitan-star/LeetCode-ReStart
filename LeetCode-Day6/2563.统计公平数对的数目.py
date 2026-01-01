# 题目链接：https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/
# 暴力解法----“超出时间限制”
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         ans = 0
#         for i,num in enumerate(nums):
#             for j in range(i+1,len(nums)):
#                 if lower <= (nums[i] + nums[j]) and  (nums[i] + nums[j]) <= upper:
#                     ans += 1
#         return ans
from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def binsearch(self, nums: List[int], n: int, x: int, left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] + x < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        # 二分查找两个目标
        # 1、找到mid下标+当前值 >= lower的第一个位置
        # 2、找到mid下标+当前值 <= upper的最后一个位置
        for i in range(n):
            x = nums[i]
            left = self.binsearch(nums, n, x, i + 1, n - 1, lower)  # 第一个 >= lower-x
            right = self.binsearch(nums, n, x, i + 1, n - 1, upper + 1)  # 第一个 >  upper-x
            ans += right - left
        return ans