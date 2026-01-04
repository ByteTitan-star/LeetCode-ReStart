# 题目链接：https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/
from collections import defaultdict
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        cnt = defaultdict(int)
        for i,num in enumerate(nums):
            if cnt[-num] > 0:
                ans = max(ans,abs(num))
            cnt[num]+=1
        return ans

if __name__ == '__main__':
    print(Solution().findMaxK([-1,2,-3,3]))