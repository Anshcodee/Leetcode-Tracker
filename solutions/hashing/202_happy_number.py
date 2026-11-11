# Relatively simple
# To learn - Difference between array and hash set
'''
Hash Set - Uses hash table to get values. Just like a dictionary
Only includes unique numbers!
Unordered at default
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #This is a hash set for better time complexity than a list
        if n == 1: return True
        seen.add(n) # For list we use append, this is for hash set
        while n>1:
            n = self.convertn(n)
            if n in seen:
                return False
            elif n==1:
                return True
            else:
                seen.add(n)

    def convertn(self, n: int) -> int:
        res = 0
        while n>0:
            temp = n%10
            res += temp**2
            n=n//10
        return res        
