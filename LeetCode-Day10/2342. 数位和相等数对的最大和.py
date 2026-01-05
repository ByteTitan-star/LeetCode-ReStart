# 题目链接：https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
from collections import defaultdict
from typing import List


class Solution:
    def swSum(self,num:int) -> int:
        x = 0
        while num :
            x += num%10
            num//=10
        return x
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        cnt = defaultdict(int)  # 存最大值
        cnt[self.swSum(nums[0])] = nums[0]
        print(nums[0],self.swSum(nums[0]),cnt[self.swSum(nums[0])],ans)
        for i in range(1,n):
            x = self.swSum(nums[i])
            if cnt[x] > 0:
                ans = max(ans,cnt[x]+nums[i])
                cnt[x] = max(cnt[x],nums[i])
            else:cnt[x] = nums[i]
        return ans

if __name__ == '__main__':
    print(Solution().maximumSum([18,43,36,13,7]))