# 题目链接：https://leetcode.cn/problems/minimum-discards-to-balance-inventory/description/
from collections import Counter
from typing import List

# 方法一：会time out
# class Solution:
#     def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
#         # w就是滑动窗口的长度，m就是允许同一商品出现的次数
#         # 返回需要丢弃的物品数量
#         ans = 0
#         n = len(arrivals)
#         cnt = Counter()
#         for i in range(w):
#             cnt[arrivals[i]] += 1       # 保留 or 丢弃
#             if cnt[arrivals[i]] > m:
#                 ans += 1
#                 cnt[arrivals[i]] -= 1   # 丢弃
#         for i in range(w, n):
#             cnt[arrivals[i - w]] -= 1
#             cnt[arrivals[i]] += 1
#             if cnt[arrivals[i]] > m:
#                 ans += 1
#         return ans

# 方法二、优化维护方式
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        ans = 0
        cnt = Counter()
        for i in range(w):
            if cnt[arrivals[i]] == m:
                arrivals[i] = 0  # 软删除，用0代表丢弃
                ans += 1
            else:
                cnt[arrivals[i]] += 1
        for i in range(w, n):
            if arrivals[i - w] != 0:
                cnt[arrivals[i - w]] -= 1
            if cnt[arrivals[i]] == m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[arrivals[i]] += 1

        return ans
if __name__ == '__main__':
    print(Solution().minArrivalsToDiscard([1,2,1,3,1],4,2))