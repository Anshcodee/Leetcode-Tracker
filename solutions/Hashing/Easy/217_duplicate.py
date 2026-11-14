# Quite ez with hashing
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
    '''
    M2:
    Use seen = set()
    Replace line 7 with seen.add(num)
    '''