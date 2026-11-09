class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
#M1
        seen = {}
# enumerate takes index(i) and list vals - it returns a dictionary with list vals paried with indices as keys
        for i, num in enumerate(nums): 
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
# if not present then put it in the dictionary
            seen[num] = i