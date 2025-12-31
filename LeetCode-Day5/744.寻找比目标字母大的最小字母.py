# 题目链接：https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if left == n or letters[left] < target:
            return letters[0]
        return letters[left]

if __name__ == '__main__':
    print(Solution().nextGreatestLetter(['c','f','j'], "a"))