# https://leetcode.cn/problems/sum-of-variable-length-subarrays/description/


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pre = [0]*n
        for i in range(1,n):
            pre[i] = pre[i-1]+nums[i-1]

        print(pre)
        for j in range(n):
            start = max(0,j-nums[j])
            print(start,pre[j]-pre[start]+nums[j])
            ans += pre[j]-pre[start]+nums[j]

        return ans
