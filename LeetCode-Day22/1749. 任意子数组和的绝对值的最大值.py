# https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
from typing import List
import math


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 计算前缀和
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        # 找到前缀和数组中的最大值和最小值
        max_pre = max(pre)
        min_pre = min(pre)

        # 最大绝对值子数组和为前缀和的最大值和最小值的差值
        return max_pre - min_pre