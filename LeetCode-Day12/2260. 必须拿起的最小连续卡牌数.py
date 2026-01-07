# 题目链接：https://leetcode.cn/problems/minimum-consecutive-cards-to-pick-up/
from collections import defaultdict
from typing import List


# 暴力
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        ans = -1
        for i in range(n):
            cnt = 0
            for j in range(i+1,n):
                if cards[j] == cards[i]:
                    if ans == -1:
                        ans = cnt
                    else:
                        ans = min(ans,cnt)
                else:
                    cnt+=1
        if ans == -1:return -1
        return ans+2

# hash+一次for
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        cnt = defaultdict(int)  # 存真实位置，下标+1
        ans = -1
        for i,card in enumerate(cards):
            if i==0:
                cnt[card] = 1
                continue
            if cnt[card] > 0:
                ans = (i+1-cnt[card]) if ans == -1 else min(ans,i+1-cnt[card])
            cnt[card] = i+1
        if ans == -1:
            return ans
        return ans+1