# 35. 搜索插入位置
def search_insert(nums, target):
    length = len(nums)
    l = 0
    r = length - 1
    while l <= r:
        mid = l + ((r - l) / 2)
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return r + 1

# def remove(nums, target):


nums = [1,2,3,3]
for value in nums:
    print(value)
nums.remove(2)
for value in nums:
    print(value)
print(len(nums))