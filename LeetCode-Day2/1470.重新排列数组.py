# 题目链接：https://leetcode.cn/problems/shuffle-the-array/description/?envType=study-plan-v2&envId=primers-list
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans

if __name__ == '__main__':
    print(Solution().shuffle([2,5,1,3,4,7],3))