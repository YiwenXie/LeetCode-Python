from typing import List

# 35. 搜索插入位置
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

# 209. 长度最小的子数组
def minSubArrayLen(s: int, nums: List[int]) -> int:
    length = len(nums)
    i = 0
    j = 0
    sum = 0
    min_length = length + 1
    while i < length:
        sum = sum + nums[i]
        while sum >= s:
            sub_length = i - j + 1
            if sub_length < min_length:
                min_length = sub_length
            sum = sum - nums[j]
            j += 1
        i += 1
    if min_length == length + 1:
        min_length = 0
    return min_length