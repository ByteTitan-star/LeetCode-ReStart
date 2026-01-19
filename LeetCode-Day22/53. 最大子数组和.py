# https://leetcode.cn/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:return nums[0]
        l = 0
        r = 0
        ans = nums[0]
        s = 0
        for r in range(l,n):
            s += nums[r]
            ans = max(ans,s)
            if s < 0:s = 0

        return ans