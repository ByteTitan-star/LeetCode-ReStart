# 题目链接：https://leetcode.cn/problems/transpose-matrix/description/?envType=study-plan-v2&envId=primers-list

from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        newMatrix = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(0,n):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix

if __name__ == '__main__':
    print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))