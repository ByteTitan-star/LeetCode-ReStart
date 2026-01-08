# 题目链接：https://leetcode.cn/problems/identify-the-largest-outlier-in-an-array/
from cmath import inf
from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        # sum = x + 2*y
        total = sum(nums)
        cnt = Counter(nums)
        ans = -inf
        for i in nums:
            t = total - i * 2
            if t in cnt and (t != i or cnt[t] > 1):
                ans = max(ans, t)
        return ans
