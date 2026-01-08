# 题目链接：https://leetcode.cn/problems/best-sightseeing-pair/description/
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = values[0]+0
        # 其实很简单，就是记录当前j下标前的最大的 value[i]+i
        preMax = ans
        for j in range(1,n):
            value = values[j]
            ans = max(ans,preMax+value-j)
            preMax = max(preMax,value+j)

        return ans


if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))