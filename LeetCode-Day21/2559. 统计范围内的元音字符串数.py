# https://leetcode.cn/problems/count-vowel-strings-in-ranges/
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        m = len(queries)
        S = ['a','e','i','o','u']
        ans = []
        pre = [0]*(n+1)
        for i in range(1,n+1):
            s = words[i-1]
            if s[0] in S and s[-1] in S:
                pre[i] = pre[i-1] + 1
            else:
                pre[i] = pre[i-1]
        for j in range(m):
            l = queries[j][0]
            r = queries[j][1]
            ans.append(pre[r+1]-pre[l])
        return ans