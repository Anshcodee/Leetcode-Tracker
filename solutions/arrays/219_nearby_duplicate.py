#Code correct, but exceeds time
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k==0: return False
        l=0
        r=1
        while l<len(nums)-1:
            if r>len(nums)-1:
                l+=1
                r=l+1
            elif (nums[l]==nums[r]):
                return True
            else: r+=1
            if (r-l > k): #Reset the window; Keeps window size below k
                l+=1
                r=l+1
        return False