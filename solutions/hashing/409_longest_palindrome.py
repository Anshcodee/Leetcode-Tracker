class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        length = 0
        for char in s:
            dic[char] = dic.get(char,0)+1
        for v in dic.values():
            if (v%2==1 and length%2==0) or (v%2==0):
                length +=v
#            else if (v%2==1) and (length%2!=0):
#               length +=(v-1)
            else:
                length +=(v-1)
        return length
                
