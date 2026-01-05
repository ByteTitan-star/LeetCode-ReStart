# 题目链接：https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        cnt[nums[0]] = 1
        ans = 0
        for i,num in enumerate(nums):
            if i == 0: continue
            if cnt[k-num] > 0:
                ans += 1
                cnt[k-num] -=1
            else:cnt[num] += 1
        return ans


if __name__ == '__main__':
    print(Solution().maxOperations([1,2,3,4],5))