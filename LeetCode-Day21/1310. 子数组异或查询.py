# https://leetcode.cn/problems/xor-queries-of-a-subarray/description/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        m = len(queries)
        ans = []
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ arr[i]

        print(pre)
        for j in range(m):
            l = queries[j][0]
            r = queries[j][1]
            ans.append(pre[r + 1] ^ pre[l])

        return ans