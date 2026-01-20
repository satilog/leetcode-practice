def best_bubble(nums, ascending=True):
    no_of_swaps = 0
    for i in range(0,len(nums)-1):
        swapped = False
        for j in range(0, len(nums)-1 - i):
            # print(i, j)
            if (ascending and nums[j] > nums[j + 1]) or (not ascending and nums[j] < nums[j + 1]):
                swapped = True
                no_of_swaps += 1
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not swapped:
            break
    print(nums, "Asc: " if ascending == True else "Desc")
    return no_of_swaps 


N = int(input())

# Ensure input is space separated to distinguish between different numbers
nums = list(map(int, input().split()))

print(nums)

swaps_asc = best_bubble(nums, ascending=True)
swaps_desc = best_bubble(nums, ascending=False)

print(min(swaps_asc, swaps_desc))
