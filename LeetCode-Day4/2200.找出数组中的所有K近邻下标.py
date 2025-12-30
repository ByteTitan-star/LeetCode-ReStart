# 提目链接：https://leetcode.cn/problems/find-all-k-distant-indices-in-an-array/description/
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (abs(i-j)<=k and nums[j] == key):
                    ans.append(i)
                    break
        return ans

if __name__ == '__main__':
    print(Solution().findKDistantIndices([3,4,9,1,3,9,5],9,1))