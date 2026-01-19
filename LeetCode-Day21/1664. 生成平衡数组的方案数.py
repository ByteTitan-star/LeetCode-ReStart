# https://leetcode.cn/problems/ways-to-make-a-fair-array/description/
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = s = 0
        for i, x in enumerate(nums):
            s += x if i % 2 else -x
        for i, x in enumerate(nums):
            s -= x if i % 2 else -x
            ans += s == 0
            s -= x if i % 2 else -x
        return ans