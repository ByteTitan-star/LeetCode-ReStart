# 题目链接：https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = 0
        for i in range(k):
            avg += arr[i]
        maxAvg = avg / k
        ans = 1 if maxAvg >= threshold else 0
        for i in range(k,len(arr)):
            avg = avg + arr[i] - arr[i-k]
            maxAvg = avg / k
            if maxAvg >= threshold:
                ans+=1
        return ans

if __name__ == '__main__':
    print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))