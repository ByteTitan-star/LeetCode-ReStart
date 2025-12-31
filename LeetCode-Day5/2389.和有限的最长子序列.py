# 题目链接：https://leetcode.cn/problems/longest-subsequence-with-limited-sum/description/
from typing import List
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = []
        nums.sort()
        for i,target in enumerate(queries):
            left = 0
            cnt = 0
            acc = 0
            for j,num in enumerate(nums):
                acc += num
                while left <= j and acc > target:
                    acc -= nums[left]
                    left += 1
                cnt = max(cnt,j-left+1)
            ans.append(cnt)
        return ans

if __name__ == '__main__':
    print(Solution().answerQueries([4,5,2,1],[3,10,21]))