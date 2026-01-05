# 题目链接：https://leetcode.cn/problems/maximum-distance-in-arrays/
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 全局最大、最小及其行号
        max_val = max(arrays[i][-1] for i in range(len(arrays)))
        min_val = min(arrays[i][0] for i in range(len(arrays)))
        max_row = next(i for i in range(len(arrays)) if arrays[i][-1] == max_val)
        min_row = next(i for i in range(len(arrays)) if arrays[i][0] == min_val)

        if max_row != min_row:
            return max_val - min_val

        # 冲突了，找次大或次小
        second_max = max(arrays[i][-1] for i in range(len(arrays)) if i != max_row)
        second_min = min(arrays[i][0] for i in range(len(arrays)) if i != min_row)

        return max(second_max - min_val, max_val - second_min)

if __name__ == '__main__':
    print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]]))