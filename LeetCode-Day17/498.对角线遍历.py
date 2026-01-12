# 题目链接：https://leetcode.cn/problems/diagonal-traverse/description/
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # i+j在一条线上，就是一个对角线
        n = len(mat)
        m = len(mat[0])
        ans = []
        arr = {}
        for i in range(n):
            for j in range(m):
                if i+j not in arr:
                    arr[i+j] = []
                arr[i+j].append(mat[i][j])

        for k,v in arr.items():
            if k%2!=1:
                v = v[::-1]
            for num in v:
                ans.append(num)

        return ans


# 对角线遍历后，按照i+j进行存储，并通过reverse等思想尾加元素就可以