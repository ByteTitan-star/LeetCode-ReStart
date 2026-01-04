# 题目链接：https://leetcode.cn/problems/number-of-good-pairs/
# 一次for循环
from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = defaultdict(int)
        for i in range(n):
            ans += cnt[nums[i]]
            cnt[nums[i]]+=1
        return ans

if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))