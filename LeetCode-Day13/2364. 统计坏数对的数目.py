# 题目链接：https://leetcode.cn/problems/count-number-of-bad-pairs/
from collections import defaultdict
from typing import List


# 解法一：暴力超时  50 / 65 个通过的测试用例
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # 暴力
        n = len(nums)
        ans = 0
        if n == 1:return 0
        for j in range(1,n):
            for i in range(0,j):
                if j-i != nums[j]-nums[i]:
                    ans += 1
        return ans


# 算法二、哈希维护
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:return 0
        ans = 0
        cnt = defaultdict(int)
        #  j - i != nums[j] - nums[i]换成 nums[i]-i != nums[j] - j
        #  所以cnt存的key是nums[i]-i  value存的是次数
        for j,num in enumerate(nums):
            ans += (j-cnt[num-j])
            cnt[num-j]+=1

        return ans


if __name__ =='__main__':
    print(Solution().countBadPairs([1,2,3,4,5]))