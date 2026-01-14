# https://leetcode.cn/problems/sum-of-beauty-in-the-array/

# 暴力 time out
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n-1):
            flag2 = 2 # 上述处理完美丽值为1的情况
            j,k = i-1,i+1
            while j >= 0:
                if nums[j] >= nums[i]:
                    flag2 = 0
                    break
                j-=1
            while k<=n-1:
                if nums[k] <= nums[i]:
                    flag2 = 0
                    break
                k+=1
            # 上述处理完美丽值为2的情况
            if flag2 != 2:
                ans += 1 if nums[i] > nums[i-1] and nums[i] < nums[i+1] else 0
            ans += flag2
        return ans

# left_max 和 right_min，分别记录每个位置左侧的最大值和右侧的最小值
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pre,suf = [0]*n,[0]*n # pre记录当前下标前的最大值  suf记录当前下标后的最小值
        for i in range(1,n):
            pre[i] = max(pre[i-1],nums[i-1]) # 当前下标前的最大值
        for j in range(n-2,-1,-1):
            suf[n-1] = inf
            suf[j] = min(suf[j+1],nums[j+1])
        print(pre,suf)
        for i in range(1,n-1):
            flag2 = 2
            if nums[i] <= pre[i] or nums[i] >= suf[i]:
                flag2 = 0
            # 上述处理完美丽值为2的情况
            if flag2 != 2:
                ans += 1 if nums[i] > nums[i-1] and nums[i] < nums[i+1] else 0
            ans += flag2
        return ans