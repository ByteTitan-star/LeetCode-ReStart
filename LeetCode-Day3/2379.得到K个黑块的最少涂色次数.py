# 题目链接：https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 情节分析，就是求滑动窗口为k的白色最小有多少个
        # 解法1：hash
        # hash = {'W':0,'B':0}
        # for i in range(0,k):
        #     hash[blocks[i]] += 1
        # ans = hash['W']
        # for i in range(k,len(blocks)):
        #     hash[blocks[i]] += 1
        #     hash[blocks[i-k]] -= 1
        #     ans = min(ans,hash['W'])
        # return ans
        # 解法2：滑动窗口
        sub_blocks = blocks[:k]
        ans = sub_blocks.count('W') # 求字符串中字符出现的次数
        cnt = ans
        for i in range(k,len(blocks)):
            cnt += 1 if blocks[i] =='W' else 0
            cnt -= 1 if blocks[i-k] == 'W' else 0
            ans = min(ans,cnt)
        return ans
if __name__ == '__main__':
    print(Solution().minimumRecolors("WBBWWBBWBW",7))