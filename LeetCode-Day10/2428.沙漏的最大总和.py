# 题目链接：https://leetcode.cn/problems/maximum-sum-of-an-hourglass/description/
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 沙漏大小就是3*3的矩阵，去除
        ans = 0
        for i in range(2,m):
            for j in range(2,n):
                ans = max(ans,grid[i-2][j-2]+grid[i-2][j-1]+grid[i-2][j]+grid[i-1][j-1]+grid[i][j-2]+grid[i][j-1]+grid[i][j])

        return ans

if __name__ == '__main__':
    print(Solution().maxSum([[1,2,3],[4,5,6],[7,8,9]]))