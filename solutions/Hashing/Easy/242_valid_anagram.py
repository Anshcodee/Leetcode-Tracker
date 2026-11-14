class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for alph in t:
            if (alph in dic) and (dic[alph]>0):
                dic[alph] -=1
            else: return False
        for vals in dic.values():
            if vals is not 0:
                return False
        return True