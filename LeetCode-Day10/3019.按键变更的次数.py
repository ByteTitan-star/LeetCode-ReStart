# 题目链接：https://leetcode.cn/problems/number-of-changing-keys/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        s = s.lower()
        ans = 0
        for i in range(1,n):
            if s[i-1] != s[i]: ans+=1
        return ans

if __name__ == '__main__':
    print(Solution().countKeyChanges("aAbBcC"))
