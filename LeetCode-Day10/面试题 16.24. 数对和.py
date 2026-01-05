# 题目链接：https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
from collections import defaultdict
from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:return []
        ans = []
        cnt = defaultdict(int)
        cnt[nums[0]] = 1
        for i in range(1,n):
            x = nums[i]
            if cnt[target-x] > 0:
                ans.append([target-x,x])
                cnt[target-x] -=1
            else:
                cnt[x] += 1
        return ans


if __name__ == '__main__':
    print(Solution().pairSums([5,6,5],11))