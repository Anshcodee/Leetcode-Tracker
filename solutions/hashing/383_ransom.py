class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        usable_words = {}
        for char in magazine:
            if char not in usable_words:     #
                usable_words[char] = 1       # This part can be just a simple addition
            else:                            #
                usable_words[char] +=1       # Using dic.get(char,0)+1
        for char in ransomNote:
            if (char not in usable_words) or (char in usable_words and usable_words[char] < 1):
                return False
            else:
                usable_words[char] -=1
        return True        
        
'''M2:        
        if len(ransomNote) > len(magazine):
            return False
        dic = {}
        for alph in magazine:
            dic[alph] = dic.get(alph,0)+1
        for alph in ransomNote:
            if (alph in dic) and (dic[alph]>0):
                dic[alph] -= 1
            else: return False
        return True
'''        