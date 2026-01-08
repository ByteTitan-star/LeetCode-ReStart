# 题目链接：https://leetcode.cn/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/description/
from cmath import inf

from numba import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = mx = -inf
        mn = inf
        for i in range(m - 1, len(nums)):
            # 维护左边 [0,i-m+1] 中的最小值和最大值
            y = nums[i - m + 1]
            mn = min(mn, y)
            mx = max(mx, y)
            # 枚举右
            x = nums[i]
            ans = max(ans, x * mn, x * mx)
        return ans