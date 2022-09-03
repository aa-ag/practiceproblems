def rotate(nums: list[int], k: int) -> None:
    """
     Do not return anything, modify nums in-place instead.
    """
    # for i in range(k):
    #     temp = nums.pop(-1)
    #     nums.insert(0, temp)
    
    # return nums
    n = len(nums)
    k %= n
    
    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            
            if start == current:
                break
        start += 1


print(rotate([1,2,3,4,5,6,7], 3))