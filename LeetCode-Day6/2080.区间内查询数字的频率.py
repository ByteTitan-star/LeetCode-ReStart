# 题目链接：https://leetcode.cn/problems/range-frequency-queries/
from bisect import bisect_right, bisect_left
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        cnt = defaultdict(list)  # 只要你在类的其他方法里还要用这份数据，那就定义为self.pos
        for i,num in enumerate(arr):
            cnt[num].append(i)  # 存下标
        self.cnt = cnt
    def query(self, left: int, right: int, value: int) -> int:
        cnt = self.cnt[value]
        return bisect_right(cnt,right) - bisect_left(cnt,left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
