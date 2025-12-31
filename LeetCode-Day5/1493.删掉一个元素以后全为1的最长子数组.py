# 题目链接：https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_idx = -1          # 当前窗口里那个 0 的位置
        ans = 0
        for right, x in enumerate(nums):
            if x == 0:
                # 遇到第二个 0，把 left 移到上一个 0 的后面
                left = zero_idx + 1
                zero_idx = right
            # 窗口长度 - 1 就是“删掉一个元素后的全 1 段长度”
            ans = max(ans, right - left + 1 - 1)
        # 如果数组里一个 0 都没有，也必须删一个元素，所以整体再减 0/1
        return ans if zero_idx != -1 else len(nums) - 1

if __name__ == '__main__':
    print(Solution().longestSubarray([0,1,1,1,0,1]))