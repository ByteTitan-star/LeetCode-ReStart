# 题目链接：https://leetcode.cn/problems/most-beautiful-item-for-each-query/

# 解法1：暴力   超时
# class Solution:
#     def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
#         n = len(queries)
#         ans = [0 for _ in range(n)]
#         # 先暴力
#         for j, quer in enumerate(queries):
#             target = quer
#             maxBeaut = float('-inf')
#             for i, item in enumerate(items):
#                 price = item[0]  # 当前元素的价格
#                 beaut = item[1]  # 当前元素的美丽值
#                 if price <= target:
#                     maxBeaut = max(maxBeaut, beaut)
#             ans[j] = maxBeaut if maxBeaut != float('-inf') else 0
#
#         return ans

# 解法2:2分查找
from typing import List
import bisect


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # 1. 按价格升序排序
        items.sort(key=lambda x: x[0])

        # 2. 构建价格数组与前缀最大美丽值数组
        prices = []
        prefix = []
        max_so_far = 0
        for price, beauty in items:
            prices.append(price)
            max_so_far = max(max_so_far, beauty)
            prefix.append(max_so_far)

        # 3. 回答每个查询
        ans = []
        for q in queries:
            # 找到最后一个 price <= q 的下标
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:
                ans.append(prefix[idx])
            else:
                ans.append(0)
        return ans

if __name__ == '__main__':
    print(Solution().maximumBeauty([[1,2],[1,2],[1,3],[1,4]],[1]))