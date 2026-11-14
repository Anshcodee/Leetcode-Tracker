class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words)!=len(pattern): return False
        word_2_char = {}
        char_2_word = {}
        for i in range(len(words)):
            if words[i] not in word_2_char:
                word_2_char[words[i]] = pattern[i]
            if pattern[i] not in char_2_word:
                char_2_word[pattern[i]] = words[i]
            if (word_2_char[words[i]]!=pattern[i] or char_2_word[pattern[i]]!=words[i]): return False
        return True

'''
The following does not pass: aaaa <> dog cat cat dog:
    seen= {}    
        for i in range(len(words)):
            if (words[i] in seen) and (seen[words[i]]!=pattern[i]): return False
            else if (words[i] not in seen):
                seen[words[i]] = pattern[i]

        return True'''

'''     
Working variation 2:
        dic = {}
        no = 0
        for ch in pattern:
            if ch not in dic:
                no += 1
                dic[ch] = no
        # Atp, keys are characters 'abbca', vals are the index of the first occurence.
        # So a character maps to it's first appearance only here
        ind = 1
        work = s.split(" ")
        # What we will do now is map the character to it's string and check the rest
        for i in range(len(s)):
            for k,v in dic.items():
                if i in v:
                    k == work[i]
                elif work[i] in k:
                    continue
'''
