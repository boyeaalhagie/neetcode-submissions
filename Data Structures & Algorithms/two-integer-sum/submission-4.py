class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return []

        # finding the complement
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in nums and nums.index(nums[i]) != nums.index(complement):
        #         return [i,nums.index(complement)]
        # return []



                
