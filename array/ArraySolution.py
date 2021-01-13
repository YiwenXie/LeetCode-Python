# from typing import List

# 35. 搜索插入位置
from typing import List


def search_insert(nums, target):
    length = len(nums)
    l = 0
    r = length - 1
    while l <= r:
        mid = l + ((r - l) / 2)
        if nums.index(mid) > target:
            r = mid - 1
        elif nums.index(mid) < target:
            l = mid + 1
        else:
            return mid
    return r + 1


# 27. 移除元素
def removeElement(nums: List[int], val: int) -> int:
        for num in nums:
            while nums.count(val) > 0:
                nums.remove(val)
        return len(nums)
