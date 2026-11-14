# Maximise the solution for types of candies
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
#M1: Relatively slow functioning
        res_types = set()
        res_num = 0
        for num in candyType:
            if num not in res_types:
                res_types.add(num)
                res_num +=1
                if (res_num == len(candyType)//2):
                    return res_num
        return res_num

