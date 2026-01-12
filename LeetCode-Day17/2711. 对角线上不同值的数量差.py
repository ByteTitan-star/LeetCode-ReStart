# 题目链接：https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/description/
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        st = set()
        for i in range(m):
            for j in range(n):
                # 计算 top_left[i][j]
                st.clear()
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    st.add(grid[x][y])
                    x -= 1
                    y -= 1
                top_left = len(st)

                # 计算 bottom_right[i][j]
                st.clear()
                x, y = i + 1, j + 1
                while x < m and y < n:
                    st.add(grid[x][y])
                    x += 1
                    y += 1
                bottom_right = len(st)

                ans[i][j] = abs(top_left - bottom_right)
        return ans