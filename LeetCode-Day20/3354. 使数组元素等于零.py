# https://leetcode.cn/problems/make-array-elements-equal-to-zero/

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # 这道题可以转换一下
        # 下标0的左边和右边之和的 相等或其他两种情况
            #（左 = 右+1 先向左）
            #（右 = 左+1 先向右）
        n = len(nums)
        ans = 0
        pre,suf = [0]*n,[0]*n  # pre存的是当前下标前的和;suf存的是当前下标后的和
        for i in range(1,n):
            pre[i] = pre[i-1]+nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j] = suf[j+1]+nums[j+1]
        for i in range(0,n):
            if nums[i] != 0: continue
            if pre[i] == suf[i]: ans += 2
            elif pre[i] == (suf[i]+1): ans += 1 # 仅先向左
            elif (pre[i]+1 == suf[i]): ans += 1 # 仅先向右

        return ans