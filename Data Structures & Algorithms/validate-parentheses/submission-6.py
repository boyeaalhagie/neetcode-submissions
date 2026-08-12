class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        CloseToOpen={"}":"{",")":"(","]":"["}

        for c in s:
            # if open check
            if c in CloseToOpen:
                # check if the open is in the stack
                if stack and CloseToOpen[c]==stack[-1]:
                    stack.pop()
                else:
                    return False                
                
            # else add
            else:
                stack.append(c)
            
        return True if not stack else False