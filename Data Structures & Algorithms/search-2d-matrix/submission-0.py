class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [x for sub in matrix for x in sub]
        l,r=0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False