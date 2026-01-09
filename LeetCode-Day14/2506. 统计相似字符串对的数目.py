# 题目链接：https://leetcode.cn/problems/count-pairs-of-similar-strings/description/
from typing import List


# 26个英文字母
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 暴力
        n = len(words)
        ans = 0
        for i in range(n):
            cnt1 = [0 for _ in range(26)]
            for ch in words[i]:
                cnt1[ord(ch)-ord('a')]+= 1  # words[i] 仅由小写英文字母组成
            for j in range(i + 1, n):
                cnt2 = [0 for _ in range(26)]
                for ch in words[j]:
                    cnt2[ord(ch)-ord('a')] += 1
                # 检查两个计数数组是否完全相同
                if all((cnt1[k] > 0 and cnt2[k] > 0) or (cnt1[k] == 0 and cnt2[k] == 0) for k in range(26)):
                    ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().similarPairs([["aba","aabb","abcd","bac","aabc"]]))
