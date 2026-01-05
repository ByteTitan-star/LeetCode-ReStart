# 题目链接：https://leetcode.cn/problems/number-of-common-factors/description/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x = min(a,b)
        ans = 0
        for i in range(1,x+1):
            if a%i ==0 and b %i ==0:
                ans += 1
        return ans

if __name__ == '__main__':
    print(Solution().commonFactors(12,6))