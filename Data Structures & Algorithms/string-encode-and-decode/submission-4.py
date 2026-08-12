class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        print(s)
        return(s)


    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            l=int(s[i:j])
            start=j+1
            end=j+1+l
            res.append(s[start:end])
            i=end
        
        return res