# Important q for getting hang of sets/hash sets
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        # set3 = set("zxcvbnm")
        res = []
        for char in words:
            newchar = char.lower()
            counter1 = 0
            counter2 = 0
            for letter in newchar:
                if (letter in set1):
                    counter1+=1
                elif (letter in set2):
                    counter2+=1
            if counter1 == len(char) or counter2 == len(char) or (counter1 == 0 and counter2 == 0):
                res.append(char)
        return res