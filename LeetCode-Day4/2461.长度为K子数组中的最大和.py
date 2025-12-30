# 题目链接：https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxAns = 0
        accumulate = 0
        cnt = Counter()
        unique = 0
        for i in range(k):
            accumulate += nums[i]
            if cnt[nums[i]] == 0: unique+=1
            cnt[nums[i]]+=1
        if unique == k: maxAns = accumulate
        for i in range(k,n):
            accumulate += (nums[i]-nums[i-k])
            if cnt[nums[i-k]]<=1:unique-=1
            cnt[nums[i-k]]-=1
            if cnt[nums[i]] == 0:unique+=1
            cnt[nums[i]]+=1
            if unique == k:maxAns = max(maxAns,accumulate)
        return maxAns

if __name__ == '__main__':
    print(Solution().maximumSubarraySum([1,5,4,2,9,9,9],3))