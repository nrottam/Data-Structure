# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def searchInsert(nums, target: int) -> int:
    l = len(nums)
    if nums[l//2] == target:
        return l//2
    elif nums[l//2] > target:
        searchInsert(nums[:l//2], target)
    elif nums[l//2] < target:
        searchInsert(nums[l//2:], target)
    else:
        nums.append(target)
        nums.sort()
        searchInsert(nums,target)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    searchInsert([1,3,5,6], target = 5)

