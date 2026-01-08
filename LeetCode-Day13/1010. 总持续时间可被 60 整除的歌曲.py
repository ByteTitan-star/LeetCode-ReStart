# 题目链接：https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        ans = 0
        cnt = defaultdict(int)
        for t in time:
            x = t % 60
            if x == 0:
                ans += cnt[0]
            else:
                ans += cnt[60-x]
            cnt[x] += 1

        return ans
