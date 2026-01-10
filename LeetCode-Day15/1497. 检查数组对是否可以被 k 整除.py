# 题目链接：https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/description/
# 暴力   肯定超时
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         n = len(arr)
#         use = [0]*n
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if use[j] == 0 and (arr[i]+arr[j])%k == 0:
#                     use[i] = 1
#                     use[j] = 1
#         for i in range(n):
#             if use[i] == 0:
#                 return False
#         return True
from collections import defaultdict
from typing import List


# 模拟
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 考虑到k 的范围有限
        # 特殊情况1:0 只要是整数就可以
        # 特殊情况2:如果k能被2整除，k/2 要是偶数
        # 特殊情况3: 1 and k-1   2 and k-2数量要匹配上，

        n = len(arr)
        cnt = defaultdict(int)
        for x in arr:
            cnt[x%k]+=1
        if cnt[0]%2!=0:return False  # 特殊情况1
        for i in range(1,k//2+1):
            if k%2==0 and i == k//2 and cnt[i]%2!=0:return False   # 特殊情况2
            if cnt[i] != cnt[k-i]:    # 特殊情况3
                return False

        return True

if __name__ == '__main__':
    print(Solution().canArrange([1,2,3,4,5,6,7,8,9], 2))