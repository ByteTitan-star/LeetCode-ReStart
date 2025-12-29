# 题目链接：https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        for i in range(k):
            if s[i] in "aeiou":
                cnt += 1
        maxCnt = cnt
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                cnt += 1
            if s[i-k] in "aeiou":
                cnt -= 1
            maxCnt = max(maxCnt,cnt)
        return maxCnt

if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef",3))