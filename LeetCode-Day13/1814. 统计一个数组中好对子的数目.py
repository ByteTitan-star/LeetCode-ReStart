# 题目链接：https://leetcode.cn/problems/count-nice-pairs-in-an-array/description/
from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1e9+7
        ans = 0
        cnt = defaultdict(int)
        for i in range(n):
            num = nums[i]
            rnum = int(str(num)[::-1])
            ans += cnt[num-rnum]
            cnt[num-rnum] += 1

        return int(ans%MOD)


if __name__ == '__main__':
    s = Solution()
    print(s.countNicePairs([42,11,1,97]))