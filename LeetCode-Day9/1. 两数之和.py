# 题目链接：https://leetcode.cn/problems/two-sum/submissions/688906120/
from typing import List


# 暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1,-1]

# 优化维护
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        cnt = {}
        for i,num in enumerate(nums):
            if target-num in cnt:
                return [cnt[target-num],i]
            cnt[num] = i
        return [0,0]


if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15],9))