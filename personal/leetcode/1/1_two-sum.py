class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], idx]
            nums_map[num] = idx