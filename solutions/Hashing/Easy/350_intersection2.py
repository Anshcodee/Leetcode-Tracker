# Quite easy
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        res = []
        for num in nums1:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] +=1
        for num in nums2:
            if num in seen and seen[num]>0:
                res.append(num)
                seen[num] -=1
        return res