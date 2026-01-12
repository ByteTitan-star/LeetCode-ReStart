# https://leetcode.cn/problems/minimum-average-difference/
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # 存前缀平均值和后缀平均值和
        pre,suf = [0]*n,[0]*n
        min_S = inf
        ans = 0
        for i in range(n):
            if i == 0:
                pre[0] = nums[0]
            else:
                pre[i] = (nums[i]+pre[i-1])
        for j in range(n-1,-1,-1):
            if j == n-1:
                suf[n-1] = nums[j]
            else:
                suf[j] = (nums[j]+suf[j+1])
        print(pre,suf)
        for k in range(n-1):
            if k == 0:
                min_S = abs(pre[k] - suf[k+1]//(n-1))
                ans = k
            else:
                if abs(pre[k]//(k+1) - suf[k+1]//(n-k-1)) < min_S:
                    min_S = abs(pre[k]//(k+1) - suf[k+1]//(n-k-1))
                    ans = k
        # 处理最后一个分割点
        if abs(pre[-1] // n) < min_S:
            ans = n - 1
        return ans