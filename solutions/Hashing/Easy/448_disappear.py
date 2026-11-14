class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:       
        numbers = set()       
        for i in range(len(nums)):
            numbers.add(i+1) # This avoids adding a zero
        for num in nums:
            numbers.discard(num)
        res = list(numbers)
        return res     

'''
Faster hash set approach:
        seen = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in seen]
'''

'''
Thoughtful(Impressive approach): Make the indices of the occuring elements as -ve
        # Pass 1: Mark seen numbers by negating the value at their corresponding index
        for num in nums:
            idx = abs(num) - 1       # 1. abs() recovers the original number if it was already marked negative
            if nums[idx] > 0:        # 2. Only flip if positive (prevents double-negating duplicates back to positive!)
                nums[idx] = -nums[idx]
                
        # Pass 2: Any index still holding a positive number was never visited
        return [i + 1 for i, num in enumerate(nums) if num > 0]
'''

''' M2: Takes very long
        res = []
        for i in range(len(nums)):
            if (i+1) not in nums:
                res.append(i+1)
        return res
'''