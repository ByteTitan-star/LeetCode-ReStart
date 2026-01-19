# https://leetcode.cn/problems/range-sum-query-immutable/description/


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.pre = [0]*n
        for i in range(1,n):
            self.pre[i] = self.pre[i-1]+nums[i-1]  # 前缀和

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right]-self.pre[left] + self.nums[right]
