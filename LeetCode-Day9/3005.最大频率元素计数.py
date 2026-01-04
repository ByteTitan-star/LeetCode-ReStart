# 题目链接：https://leetcode.cn/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2026-01-04
from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        ans = 0
        maxCnt = 0
        for i, num in enumerate(nums):
            cnt[num] += 1
            maxCnt = max(maxCnt, cnt[num])
        for i, num in enumerate(nums):
            if cnt[num] == maxCnt:
                ans += cnt[num]
                cnt[num] = 0
        return ans


if __name__ == '__main__':
    print(Solution().maxFrequencyElements([1,2,2,3,1,4]))