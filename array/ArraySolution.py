class Solution:
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
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.remove(val)