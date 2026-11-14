class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for alph in s:
            if alph not in dic:
                dic[alph] = 1
            else:
                dic[alph] += 1
        for key, val in dic.items():
            if val == 1:
                return (s.index(key))
        return -1

''' M2: Instead of frequency lists, we're holding all positions
    Simpler but worse performance        
        dic = {} # It's not a frequency list, contains all indices of a char
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = []
            dic[s[i]].append(i)
        for k,v in dic.items():
            if len(v) == 1:
                return v[0]
        return -1'''