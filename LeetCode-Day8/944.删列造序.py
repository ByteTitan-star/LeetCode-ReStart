# 题目链接：https://leetcode.cn/problems/delete-columns-to-make-sorted/description/?envType=daily-question&envId=2026-01-03
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        n = len(strs)
        for j in range(len(strs[0])):
            for i in range(1, n):
                if strs[i][j] < strs[i - 1][j]:
                    ans += 1
                    break
        return ans

if __name__ == '__main__':
    print(Solution().minDeletionSize(["cba","daf","ghi"]))