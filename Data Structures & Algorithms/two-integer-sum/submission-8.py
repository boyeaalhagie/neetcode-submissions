class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]
        # return []

        # hasmap
        hashmap = {}

        for i,n in enumerate(nums):
            dif = target - n
            if dif in hashmap:
                return [hashmap[dif],i]
            hashmap[n]=i



                
