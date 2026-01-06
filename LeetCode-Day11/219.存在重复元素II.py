# 题目链接：https://leetcode.cn/problems/contains-duplicate-ii/description/
from collections import defaultdict
from typing import List


# 解法一：暴力   超时
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if i==j:continue
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True
#         return False

# 解法二：for维护
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cnt = defaultdict(int)  # 存下标+1
        for i,num in enumerate(nums):
            if i == 0 :
                cnt[num] = 1  # 真实位置从1开始计算，如果从0开始计算的话，会冲突
                continue
            if cnt[num] > 0:# 意味着有数据
                if abs((i+1)-cnt[num]) <= k:
                    return True
                else: # 更新真实位置
                    cnt[num] = i+1
            else:
                cnt[num] = i+1

        return False

if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1],3))