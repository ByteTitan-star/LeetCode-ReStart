# https://leetcode.cn/problems/number-of-good-ways-to-split-a-string/description/
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        ans = 0
        pre_diff = [0]*n
        suf_diff = [0]*n
        temp = set({})  # set
        for i in range(0,n):
            if i == 0:
                pre_diff[0] = 1
            else:
                if s[i] not in temp:
                    pre_diff[i] = pre_diff[i-1]+1
                else:
                    pre_diff[i] = pre_diff[i-1]
            temp.add(s[i])
        temp.clear()
        for j in range(n-1,-1,-1):
            if j == n-1:suf_diff[j] = 1
            else:
                if s[j] not in temp:
                    suf_diff[j] = suf_diff[j+1] + 1
                else:
                    suf_diff[j] = suf_diff[j+1]
            temp.add(s[j])
        for i in range(0,n-1):
            if pre_diff[i] == suf_diff[i+1]:
                ans += 1
        return ans