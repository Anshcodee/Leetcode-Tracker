#Need to understand/review
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in dic_s:
                dic_s[char_s] = i
            if char_t not in dic_t:
                dic_t[char_t] = i
            
            if dic_s[char_s]!=dic_t[char_t]: #Core logic
                return False
        
        return True

    '''
    Eg:
    For pop and boo (instead of bob)
    Index i = 2 (char_s = 'p', char_t = 'o')
    'p' is already in dic_s, so dic_s['p'] remains 0 (its first occurrence).
    'o' is already in dic_t, so dic_t['o'] remains 1 (its first occurrence).
    Check: dic_s['p'] != dic_t['o'] (0 != 1) --> Mismatch found! Returns False.
    '''


    ''' Time-heavy approach >>>
        dic_s = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in dic_s:
                dic_s[ch] = []
            dic_s[ch].append(i)
        
        dic_t = {}
        for i in range(len(t)):
            ch = t[i]
            if ch not in dic_t:
                dic_t[ch] = []
            dic_t[ch].append(i)
        return list(dic_s.values()) == list(dic_t.values())'''
        # Issue above: Too much time taken to append each index
        # Can be improved - We can run this in one for loop instead of 2
    