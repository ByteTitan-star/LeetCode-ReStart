# https://leetcode.cn/problems/number-of-ways-to-split-array/description/
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left,right = [0]*n,[0]*n
        for i in range(n):
            if i == 0:
                left[0] = nums[i]
            else:
                left[i] = nums[i] + left[i-1]
        for j in range(n-1,-1,-1):
            if j == n-1:
                right[n-1] = nums[j]
            else:
                right[j] = nums[j] + right[j+1]
        for k in range(0,n-1):
            if left[k] >= right[k+1]:
                ans += 1

        return ans