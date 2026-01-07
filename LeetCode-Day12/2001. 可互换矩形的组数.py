# 题目链接：https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/
from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        n = len(rectangles)
        cnt = defaultdict(int)
        ans = 0
        for width,hegiht in rectangles:
            cnt[width/hegiht] += 1
        for k,v in cnt.items():
            if v>=2:
                ans += v*(v-1)//2
        return ans



if __name__ == '__main__':
    print(Solution().interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))