class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        CloseToOpen={"}":"{",")":"(","]":"["}

        for char in s:
            # check if the char is in close
            if char in CloseToOpen:
                # check if it closes the open
                if stack and stack[-1]==CloseToOpen[char]:
                    stack.pop()
                # return False
                else:
                    return False

            # else add it to the stack i.e its open
            else:
                stack.append(char)
        print(stack)
        return True if not stack else False