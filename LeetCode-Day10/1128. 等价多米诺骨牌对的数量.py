# 题目链接：https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        d = dict()  # 存的不是int，是元组
        ans = 0
        for d1,d2 in dominoes:
            t = tuple(sorted((d1, d2)))
            if t in d:
                d[t] += 1
            else:
                d[t] = 1   # 如果+=1会报错
        for i in d:
            ans += d[i] * (d[i]-1)//2
        return ans

if __name__ == '__main__':
    print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))