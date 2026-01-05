# 题目链接：https://leetcode.cn/problems/snapshot-array/description/
class SnapshotArray:

    def __init__(self, length: int):
        # 类数组的数据结构，初始每个元素都是0
        self.arr = [0 for _ in range(length)]
        self.snap_id = 0
        self.snapshot = []

    def set(self, index: int, val: int) -> None:
        # 将指定索引 index 处的元素设置为 val
        self.arr[index] = val

    def snap(self) -> int:
        self.snapshot.append(self.arr.copy())
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# 会超出时间限制，题目说要用二分查找，但我没读懂题意，很难知道如何使用二分