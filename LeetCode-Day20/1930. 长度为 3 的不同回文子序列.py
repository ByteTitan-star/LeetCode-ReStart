# https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0
        unorderedSet = set()
        pre, suf = defaultdict(int), defaultdict(int)
        for i in range(n - 1, 0, -1):  # 仅存下标0之后的所有元素就可以
            suf[s[i]] += 1
        pre[s[0]] += 1
        for j in range(1, n):
            x = s[j]
            suf[x] -= 1  # 当前元素先减
            for k, v in pre.items():
                if suf[k] > 0:
                    temps = k + x + k
                    if temps not in unorderedSet:
                        ans += 1
                        unorderedSet.add(temps)

            pre[x] += 1

        return ans
