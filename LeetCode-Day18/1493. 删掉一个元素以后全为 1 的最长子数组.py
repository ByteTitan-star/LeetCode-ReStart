# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # 删掉一个元素后全为1的最长子数组  等价于  列表中包含一个0的最长子数组
        left = 0
        zero = -1
        for right, x in enumerate(nums):
            if x == 0:
                left = zero + 1
                zero = right
            ans = max(ans, right - left)

        return ans if zero != -1 else len(nums) - 1


