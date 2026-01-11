# 题目链接：https://leetcode.cn/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        # 将对角线元素拿出来，排序后再放回去
        arr = {}
        for i in range(n):
            for j in range(m):
                if i - j not in arr:
                    arr[i - j] = []
                arr[i - j].append(mat[i][j])

        for value in arr.values():
            x = value.sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i - j].pop()

        return mat