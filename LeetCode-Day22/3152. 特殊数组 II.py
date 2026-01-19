# https://leetcode.cn/problems/special-array-ii/
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        m = len(queries)
        ans = []
        pre = [0]*n   # 任何下标仅和左侧元素相比，如果当前下标是偶数，pre是奇数，那就存0 否则修改为1
        for i in range(1,n):
            x = nums[i]
            prex = nums[i-1]
            if (x%2==0 and prex%2!=0) or (prex%2==0 and x%2!=0):
                pre[i] = pre[i-1]+1  # 累积记数
        print(pre)
        for j in range(m):
            l = queries[j][0]
            r = queries[j][1]
            if (r-l) != (pre[r]-pre[l]):
                ans.append(False)
            else:
                ans.append(True)
        return ans