# 题目链接：https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters/description/
class Solution:
    def check(self,s : str) -> int:
        if(s[0] != s[1] and s[1] != s[2] and s[2] != s[0]):
            return 1
        return 0
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(0,n-2):
            temps = s[i:i+3]
            if self.check(temps):
                print(temps)
                ans+=1
        return ans
if __name__ == '__main__':
    print(Solution().countGoodSubstrings("xyzzaz"))