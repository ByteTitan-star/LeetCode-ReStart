# 题目链接：https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        minValue = nums[0]
        ans = -1
        for i in range(1,n):
            if nums[i] - minValue > 0:
                ans = max(ans,nums[i]-minValue)
            minValue = min(minValue,nums[i])
        return ans


if __name__ == '__main__':
    print(Solution().maximumDifference([7,1,5,4]))