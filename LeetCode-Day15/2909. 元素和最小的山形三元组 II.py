# 题目链接：https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/description/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # 遇到 i < j < k,就是枚举中间就可以
        # 枚举j下标，前缀最小值  后  后缀最小值
        n = len(nums)
        ans = inf
        pre_min = [inf] * n
        pre_min[0] = nums[0]
        suf_min = [inf] * n
        suf_min[n - 1] = nums[n - 1]
        for i in range(1, n):
            pre_min[i] = min(pre_min[i - 1], nums[i])
        for k in range(n - 2, -1, -1):
            suf_min[k] = min(suf_min[k + 1], nums[k])
        for j in range(1, n - 1):
            if pre_min[j - 1] < nums[j] and suf_min[j + 1] < nums[j]:
                ans = min(ans, pre_min[j - 1] + nums[j] + suf_min[j + 1])
        if ans == inf: return -1
        return ans

