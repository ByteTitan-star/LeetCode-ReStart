# 题目链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口呗，来一个走一个呗
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for right,ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 1:
                cnt[s[left]] -=1
                left+=1
            ans = max(ans,right - left + 1)
        return ans

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))