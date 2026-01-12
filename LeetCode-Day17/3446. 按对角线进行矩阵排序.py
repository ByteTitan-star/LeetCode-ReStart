# 题目链接：https://leetcode.cn/problems/sort-matrix-by-diagonals/description/
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        arr = {}
        for i in range(n):
            for j in range(m):
                if i - j not in arr:
                    arr[i - j] = []
                arr[i - j].append(grid[i][j])
        for k, v in arr.items():
            if k < 0:  # 右上角
                v.sort(reverse=True)
            else:  # 左下角
                v.sort()

        for i in range(n):
            for j in range(m):
                grid[i][j] = arr[i - j].pop()

        return grid

