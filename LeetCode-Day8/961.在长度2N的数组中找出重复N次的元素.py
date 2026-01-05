# 题目链接：https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02
from collections import defaultdict
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]] += 1
            if cnt[nums[i]] == (len(nums)//2):
                return nums[i]
        return 0

if __name__ == '__main__':
    print(Solution().repeatedNTimes([1,2,3,3]))