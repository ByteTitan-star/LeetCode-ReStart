# 题目链接：https://leetcode.cn/problems/power-of-two/?envType=study-plan-v2&envId=primers-list

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        num_2 = 1
        while num_2 < n:
            num_2 = num_2 * 2
        if num_2 == n: return True
        return False

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1e9))