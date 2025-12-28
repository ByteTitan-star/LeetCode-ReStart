# 题目链接：https://leetcode.cn/problems/ugly-number/?envType=study-plan-v2&envId=primers-list
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        ugly = [2, 3, 5]
        for i in ugly:
            while n % i == 0:
                n /= i
        if n == 1: return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(100))