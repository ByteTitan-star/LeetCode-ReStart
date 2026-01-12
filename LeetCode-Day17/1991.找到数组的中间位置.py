# https://leetcode.cn/problems/find-the-middle-index-in-array/description/
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0]*n
        right_sum = [0]*n
        for i in range(1,n):
            left_sum[i] = (left_sum[i-1]+nums[i-1])

        for j in range(n-2,-1,-1):
            right_sum[j] = (right_sum[j+1]+nums[j+1])
        print(left_sum,right_sum)

        for k in range(n):
            if k == 0 and right_sum[k] == 0:return 0
            if left_sum[k] == right_sum[k]:
                return k
        return -1
