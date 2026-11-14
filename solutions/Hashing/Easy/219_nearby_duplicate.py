class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(seen[nums[i]]-i)<=k: return True
                else: 
                    seen[nums[i]] = i
            else:
                seen[nums[i]] = i
        return False