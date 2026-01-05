# 题目链接：https://leetcode.cn/problems/time-based-key-value-store/description/
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 存储给定时间戳 timestamp 时的键 key 和值 value
        self.dict[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        if len(arr) == 0 : return ""
        left = 0
        right = len(arr)-1
        if arr[left][0] > timestamp : return ""
        while left <= right:
            mid = (left+right)//2
            if arr[mid][0] < timestamp+1:
                left = mid+1
            else:
                right = mid-1
        return arr[left-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

