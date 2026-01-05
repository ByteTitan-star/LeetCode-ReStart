# 题目链接：https://leetcode.cn/problems/find-k-closest-elements/
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left,right = 0,n-1
        a,b = abs(arr[left]-x),abs(arr[right]-x)
        while right-left+1 != k:
            if a<=b:
                right-=1
                b = abs(arr[right]-x)
            else:
                left+=1
                a = abs(arr[left]-x)
        return arr[left:right+1]
