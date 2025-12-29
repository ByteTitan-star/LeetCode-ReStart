# 题目链接：https://leetcode.cn/problems/k-radius-subarray-averages/description/
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        avgs = [(-1) for _ in range(n)]
        if k >= n or (2*k+1) > n:
            return avgs
        # 重点信息提取：avgs[i]返回的是以 下标为i 为中心的子数组 半径为k的子数组平均值
        # 半径为k，实际上滑动窗口长度就是2k+1
        left = 0
        accumulate = 0
        for right in range(2 * k + 1):
            accumulate += nums[right]
        index = (2*k+1) // 2
        avgs[index] = accumulate // (2 * k + 1)
        index += 1
        for right in range(2 * k + 1, n):
            accumulate = accumulate + nums[right] - nums[left]
            avgs[index] = accumulate // (2 * k + 1)
            left += 1
            index += 1
        return avgs

if __name__ == '__main__':
    print(Solution().getAverages([7,4,3,9,1,8,5,2,6],3))