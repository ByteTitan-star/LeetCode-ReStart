# 题目链接：https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans

if __name__ == '__main__':
    print(Solution().maximumLengthSubstring("bcbbbcba"))