# 题目链接：https://leetcode.cn/problems/maximum-score-after-splitting-a-string/?envType=study-plan-v2&envId=primers-list
from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        maxAns = float('-inf')
        for i in range(1, len(s)):
            cnt = 0
            left_dict = Counter(s[:i])
            right_dict = Counter(s[i:])
            cnt = left_dict['0'] + right_dict['1']
            maxAns = max(maxAns, cnt)
        return maxAns

if __name__ == '__main__':
    print(Solution().maxScore("ab"))