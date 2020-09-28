nums = [2,7,11,15]
target = 13

def two_sum(nums):
    for i, val in enumerate(nums):
        for j in range(i+1, len(nums)):
            if val + nums[j] == target :
                return (i,j)