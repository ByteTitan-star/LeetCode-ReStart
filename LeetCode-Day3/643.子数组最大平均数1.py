# 题目链接：https://leetcode.cn/problems/maximum-average-subarray-i/description/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        for i in range(k):
            avg += nums[i]
        maxAvg = avg / k
        for i in range(k,len(nums)):
            avg = avg + nums[i] -nums[i-k]
            maxAvg = max(maxAvg,avg/k)

        return maxAvg

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3],4))