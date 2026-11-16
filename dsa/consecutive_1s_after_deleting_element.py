def consecutiveOnes(nums):
    zero_count = 0
    l = 0
    best = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[l] == 0:
                zero_count -= 1
            l += 1
        best = max(best, r - l)
    return best



print(consecutiveOnes([1, 1, 1, 0, 1, 1, 0, 0, 1, 1]))