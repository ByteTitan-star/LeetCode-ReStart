# https://leetcode.cn/problems/maximum-score-after-splitting-a-string/description/
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        cnt_1 = Counter(s)['1']
        cnt_0 = 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt_0 += 1
            else:
                cnt_1 -= 1
            ans = max(ans,cnt_0 + cnt_1)
        return ans