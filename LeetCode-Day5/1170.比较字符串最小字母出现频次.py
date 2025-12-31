# 题目链接：https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/description/
from typing import List

class Solution:
    # 超时
    # def f(self, s: str) -> int:
    #     cnt = defaultdict(int)
    #     minch = s[0]
    #     for i in range(len(s)):
    #         cnt[s[i]] += 1
    #         minch = min(minch, s[i])
    #     return cnt[minch]

    def f(self,s:str) -> int:
        return 0 if len(s)==0 else s.count(min(s))
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            count_q = self.f(queries[i])
            for j in range(len(words)):
                count_w = self.f(words[j])
                if count_q < count_w:
                    ans[i] += 1
        return ans

if __name__ == '__main__':
    print(Solution().numSmallerByFrequency(["cbd"],["zaaaz"]))
