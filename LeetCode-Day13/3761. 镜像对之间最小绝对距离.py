# 题目链接：https://leetcode.cn/problems/minimum-absolute-distance-between-mirror-pairs/
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)  # 存下标+1
        ans = inf
        for j, num in enumerate(nums):
            rnum = int(str(num)[::-1])
            if cnt[num] > 0:
                ans = min(ans, abs((cnt[num] - 1) - j))
            cnt[rnum] = j + 1

        if ans == inf: return -1
        return ans

# w了几次，分析清楚了
if __name__ == '__main__':
    print(Solution().minMirrorPairDistance([12,21,45,33,54]))