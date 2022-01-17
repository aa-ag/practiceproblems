def rotate(nums: list[int], k: int) -> None:
    """
     Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        temp = nums.pop(-1)
        nums.insert(0, temp)
    
    return nums


print(rotate([1,2,3,4,5,6,7], 3))