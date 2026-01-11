# 题目链接：https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/description/
from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        suf_cnt = Counter(s[1:])  # 统计 [1,n-1] 每个字母的个数
        pre_set = set()
        st = set()
        for i in range(1, len(s) - 1):  # 枚举中间字母 mid
            mid = s[i]
            suf_cnt[mid] -= 1  # 撤销 mid 的计数，suf_cnt 剩下的就是后缀 [i+1,n-1] 每个字母的个数
            if suf_cnt[mid] == 0:  # 后缀 [i+1,n-1] 不包含 mid
                del suf_cnt[mid]  # 从 suf_cnt 中去掉 mid
            pre_set.add(s[i - 1])  # 记录前缀 [0,i-1] 有哪些字母
            for alpha in pre_set & suf_cnt.keys():  # mid 的左右两侧都有字母 alpha
                st.add(alpha + mid)
        return len(st)
