# 题目链接：https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/submissions/688090248/
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windows = sum(cardPoints[-k:])
        ans = windows
        for i in range(k):
            windows += cardPoints[i] - cardPoints[i-k]
            ans = max(ans,windows)
        return ans

if __name__ == '__main__':
    print(Solution().maxScore([1,2,3,4,5,6,1],3))