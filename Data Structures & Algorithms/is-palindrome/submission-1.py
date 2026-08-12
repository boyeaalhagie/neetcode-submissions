class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(ch for ch in s if ch.isalnum()).lower()
        print(word)

        l,r=0,len(word)-1
        while l<r:
            if word[l] != word[r]:
                return False
            r-=1
            l+=1
        return True
        

            