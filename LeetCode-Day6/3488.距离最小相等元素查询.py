# 题目链接：https://leetcode.cn/problems/closest-equal-element-queries/description/
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        cnt = defaultdict(list)
        for i, num in enumerate(nums):
            cnt[num].append(i)          # 把所有下标按序存好

        for q in queries:
            arr = cnt[nums[q]]
            k = len(arr)
            if k <= 1:                  # 只有它自己
                ans.append(-1)
                continue

            # 找到当前查询下标 q 在 arr 中的位置
            idx = bisect_left(arr, q)   # arr 已升序
            # 前驱、后继（循环意义）
            prev = arr[(idx - 1) % k]
            nxt  = arr[idx % k] if arr[idx % k] != q else arr[(idx + 1) % k]

            # 计算循环距离
            d1 = min(abs(q - prev), n - abs(q - prev))
            d2 = min(abs(q - nxt),  n - abs(q - nxt))
            ans.append(min(d1, d2))
        return ans

if __name__ == '__main__':
    print(Solution().solveQueries([1,3,1,4,1,3,2],[0,3,5]))