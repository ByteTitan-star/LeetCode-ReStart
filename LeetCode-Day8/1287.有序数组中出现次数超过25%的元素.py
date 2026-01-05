# 题目链接：https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/
from collections import defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = defaultdict(int)
        for i,num in enumerate(arr):
            if cnt[num] > len(arr)//4:
                return num
            cnt[num] +=1
        return 1

if __name__ == '__main__':
    print(Solution().findSpecialInteger([[1,2,2,6,6,6,6,7,10]]))