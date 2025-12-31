# 题目链接：https://leetcode.cn/discuss/post/3579164/ti-dan-er-fen-suan-fa-er-fen-da-an-zui-x-3rqn/
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        ans = 0
        for i, num1 in enumerate(arr1):
            flag = True
            for j, num2 in enumerate(arr2):
                if abs(num1 - num2) <= d:
                    flag = False
                    break
            if flag: ans += 1

        return ans

if __name__ == '__main__':
    print(Solution().findTheDistanceValue([1,2,3,4,5], [1,2,3,4,5], 2))