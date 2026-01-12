# https://leetcode.cn/problems/equal-score-substrings/description/

class Solution:
    def scoreBalance(self, s: str) -> bool:
        # score = ord(s[i]) - ord('a') + 1
        n = len(s)
        left_s, right_s = [0] * n, [0] * n
        for i in range(n):
            score = ord(s[i]) - ord('a') + 1
            if i == 0:
                left_s[0] = score
            else:
                left_s[i] = left_s[i - 1] + score

        for i in range(n - 1, -1, -1):
            score = ord(s[i]) - ord('a') + 1
            if i == n - 1:
                right_s[i] = score
            else:
                right_s[i] = right_s[i + 1] + score

        for i in range(0, n - 1):
            if left_s[i] == right_s[i + 1]:
                return True
        return False
# 处理好边界条件就可以