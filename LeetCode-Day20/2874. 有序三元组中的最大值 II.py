# https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/description/
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 枚举j,找到j下标之前的前缀最大值、找到j下标后的最大值
        ans = 0
        n = len(nums)
        pre_max = [0] * n
        pre_max[0] = nums[0]  # 第一个位置的值
        suf_max = [0] * n
        suf_max[n - 1] = nums[n - 1]  # 最后一个位置的值
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], nums[i])

        for j in range(1, n - 1):
            ans = max(ans, (pre_max[j - 1] - nums[j]) * suf_max[j + 1])

        return ans