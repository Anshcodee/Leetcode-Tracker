# Relatively easy
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ## V. Faster method
        dic = {}
        res = []
        for num in nums1:
            if num not in dic:
                dic[num] = 1
        for num in nums2:
            if num in dic and (dic[num]>0):
                res.append(num)
                dic[num] -= 1
        return res

''' Hash set simple method - But takes more time
        seen = set()
        res = []
        for num in nums1:
            if num not in seen:
                seen.add(num)
        for num in nums2:
            if (num in nums2) and (num in seen):
                res.append(num)
                seen.remove(num)
        return res
'''