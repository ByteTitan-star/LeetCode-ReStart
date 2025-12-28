# 题目链接：https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/description/?envType=study-plan-v2&envId=primers-list

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right + 1):
            if words[i][0] in vowel and words[i][len(words[i]) - 1] in vowel:
                ans += 1
        return ans

if __name__ == '__main__':
    print(Solution().vowelStrings(["are","amy","u"],0,2))