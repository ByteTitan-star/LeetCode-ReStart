# 题目链接：https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/description/
from collections import defaultdict
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        # key是hours[i]   value是次数
        cnt = defaultdict(int)
        # 如果正好是24或24的倍数，我们就只存0
        for i,hour in enumerate(hours):
            hour = hour%24
            if hour == 0:
                ans += cnt[0]
            else:
                ans += cnt[24-hour]
            cnt[hour]+=1
        return ans


if __name__=='__main__':
    print(Solution().countCompleteDayPairs([12,12,30,24,24]))