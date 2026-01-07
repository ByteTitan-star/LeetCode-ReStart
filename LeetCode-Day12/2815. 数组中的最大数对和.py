# 题目链接：https://leetcode.cn/problems/max-pair-sum-in-an-array/
from collections import defaultdict
from typing import List


class Solution:
    def returnmax(self,num:int) -> int:
        x = 0
        while num:
            x = max(x,num%10)
            num//=10
        return x

    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        cnt = defaultdict(list)
        for i,num in enumerate(nums):
            x = self.returnmax(num) # 最大的数字相等
            if len(cnt[x])==0:cnt[x].append(num) # 存到list中,但是最多只存两个值（最大值，次大值）
            elif len(cnt[x])==1:
                if num < cnt[x][0]:cnt[x].append(num)
                else:
                    tmp = cnt[x][0]
                    cnt[x][0] = num
                    cnt[x].append(tmp)  # 确保一下顺序，最大值在cnt[x][0],次大值在cnt[x][1]
            else:  # list中已经有两个最大值了
                print(cnt[x][0],cnt[x][1])
                if num > cnt[x][0]:
                    tmp = cnt[x][0]
                    cnt[x][0] = num
                    cnt[x][1] = tmp
                elif num > cnt[x][1]:
                    cnt[x][1] = num
            print(num,cnt[x])

        for k,v in cnt.items():
            if len(v) == 2:
                ans = max(ans,v[0]+v[1])
        return ans


if __name__ == '__main__':
    print(Solution().maxSum([1,2,3,4,5]))