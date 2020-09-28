nums = [2,7,11,15]
target = 13

def two_sum(nums):
    for idx, val in enumerate(nums):
        for index in range(len(nums)-((idx)+1)):
            if val + nums[len(nums)-(index+1)] == target :
                return (idx, len(nums)-(index+1))