# 题目链接：https://leetcode.cn/problems/peak-index-in-a-mountain-array/description/
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left < right:
            mid = left+(right-left)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left

if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0,1,0]))