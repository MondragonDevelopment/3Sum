s = [12, 3, 1, 2, -6, 5, -8, 6]
suma = 0

def threeSum(nums, target):
    solution = []
    nums.sort()
    for num in range(len(nums) - 2):

        left = num + 1
        right = len(nums) - 1
        # I put 1 in here
        while left < right:
            curSum = nums[num] + nums[left] + nums[right] # 1
            if curSum == target:
                solution.append([nums[num], nums[left], nums[right]])
                left, right = left + 1, right - 1 # I forgot to add this line
            elif curSum < target:
                left += 1
            else:
                right -= 1
    return solution

print(threeSum(s, suma))