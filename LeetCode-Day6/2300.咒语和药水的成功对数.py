# 题目链接：https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/description/
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        ans = []
        # 只能potions数组这个进行排序
        potions.sort()
        for i,s in enumerate(spells):
            left = 0
            right = m-1
            while left <= right:
                mid = (left+right)//2
                if s*potions[mid] < success:
                    left = mid+1
                else:
                    right = mid-1
            if left < m: # 这里已经找到了大于等于success的第一个位置；剩下位置全是成功的组合
                ans.append(m-left)
            else:
                ans.append(0) # 没有成功的组合
        return ans

# 暴力解  两个for循环会超时
if __name__ == '__main__':
    print(Solution().successfulPairs([5,1,3],[1,2,3,4,5],7))