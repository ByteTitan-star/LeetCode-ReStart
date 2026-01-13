# https://leetcode.cn/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        pre,suf = [1]*n,[1]*n
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j] = suf[j+1]*nums[j+1]
        for k in range(n):
            ans[k] = suf[k]*pre[k]
        return ans