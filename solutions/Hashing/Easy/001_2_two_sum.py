class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
#M2
        seen = {}
        for i in len(nums):
            num = nums[i]
            complement = target - num

            if complement in seen:
                return [seen[complement],i]

            seen[num] = i