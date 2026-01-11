# 题目链接：https://leetcode.cn/problems/count-special-triplets/description/
from collections import defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1000000007
        ans = 0
        # 思想：首先一次遍历，存储suf_cnt，就把后缀的所有元素（去除0）入 哈希
        # 再来一次遍历，枚举j，j从1开始，这次遍历两个目标
        # suf_cnt 后缀记数器，去除当前j的元素。并维护另外一个计数器，pre_cnt(从0开始，到j)
        suf_cnt = defaultdict(int)  # 存后缀出现次数
        for k in range(n - 1, 0, -1):
            suf_cnt[nums[k]] += 1  # 第一次遍历把后缀所有元素入哈希

        pre_cnt = defaultdict(int)  # 存前缀出现次数
        pre_cnt[nums[0]] += 1  # 0号元素入哈希
        for j in range(1, n - 1):
            suf_cnt[nums[j]] -= 1
            x = nums[j] * 2
            ans += (pre_cnt[x] * suf_cnt[x])
            # 维护suf_cnt 和 pre_cnt
            pre_cnt[nums[j]] += 1

        return ans % MOD

if __name__ == '__main__':
    s = Solution()
    print(s.specialTriplets([1, 2, 3]))
