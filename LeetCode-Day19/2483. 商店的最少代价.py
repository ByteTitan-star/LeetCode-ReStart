# https://leetcode.cn/problems/minimum-penalty-for-a-shop/

# # 暴力超时
# class Solution:
#     def bestClosingTime(self, customers: str) -> int:
#         n = len(customers)
#         ans = inf
#         hour = 0
#         for i in range(0,n+1): # 关门时间
#             cnt = 0
#             for l in range(0,i):  # i坐标之前的所有的N代表代价
#                 cnt += (customers[l] == 'N')
#             for r in range(i,n):
#                 cnt += (customers[r] == 'Y')
#             if cnt < ans:
#                 ans = cnt
#                 hour = i
#         return hour

# 解法2
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre_N = [0] * (n + 1)  # pre_N[i] 表示从 0 到 i-1 位置的 'N' 的数量
        suf_Y = [0] * (n + 1)  # suf_Y[i] 表示从 i 到 n-1 位置的 'Y' 的数量
        ans = float('inf')
        hour = 0

        # 填充 pre_N 数组
        for i in range(1, n + 1):
            pre_N[i] = pre_N[i - 1] + (customers[i - 1] == "N")

        # 填充 suf_Y 数组
        for j in range(n - 1, -1, -1):
            suf_Y[j] = suf_Y[j + 1] + (customers[j] == "Y")

        # 模拟关门时间 [0, n]
        for k in range(n + 1):
            cnt = pre_N[k] + suf_Y[k]
            if cnt < ans:
                ans = cnt
                hour = k

        return hour