# 题目链接：https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/description/
from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        accumulate = 0
        maxAns = 0
        cnt = Counter()
        unique = 0
        for i in range(0, k):
            accumulate += nums[i]
            if cnt[nums[i]] == 0:
                unique += 1
            cnt[nums[i]] += 1
        if unique >= m:        maxAns = accumulate
        for i in range(k, n):
            accumulate += nums[i] - nums[i - k]
            if cnt[nums[i-k]] <= 1:   unique -= 1
            cnt[nums[i-k]] -= 1
            if cnt[nums[i]] == 0:     unique += 1
            cnt[nums[i]] += 1
            if unique >= m:        maxAns = max(maxAns,accumulate)
        return maxAns

if __name__ == '__main__':
    print(Solution().maxSum([2,6,7,3,1,7],3,4))