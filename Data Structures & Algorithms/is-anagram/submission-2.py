class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # A. Using Hashmaps

        #1. check if the lens are equal
        if len(s) != len(t):
            return False
        
        countS, countT = {},{}

        #.2 build the hashmaps with each letter and there frequencies
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #3 check the 2 hashmaps if the frequencies of each letter 
        # are the same
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True




        

        