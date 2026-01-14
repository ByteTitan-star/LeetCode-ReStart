# https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/description/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        # 枚举j
        pre,suf = [inf]*n,[inf]*n # pre存当前下标前的最小值  suf 存当前下标后的最小值
        for i in range(1,n):
            pre[i] = min(pre[i-1],nums[i-1])
        for k in range(n-2,-1,-1):
            suf[k] = min(suf[k+1],nums[k+1])
        print(pre,suf)
        for j in range(1,n):
            if nums[j] > pre[j] and nums[j] > suf[j]:  # 修正条件
                ans = min(ans,pre[j]+nums[j]+suf[j])


        return -1 if ans == inf else ans