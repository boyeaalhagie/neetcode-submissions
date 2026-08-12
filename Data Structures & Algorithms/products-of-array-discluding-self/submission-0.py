class Solution:
    
    def productExceptSelf(self, nums):
            result = []
            for i in range(len(nums)):
                temp = nums[:i] + nums[i+1:]   # all except index i
                product = 1
                for n in temp:
                    product *= n
                result.append(product)
            return result



        

        