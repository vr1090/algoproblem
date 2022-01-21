class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 2:
            return nums[0]
        
        i =0
        j = 1
        
        
        
        while j < len(nums) and nums[i] == nums[j]:
            i+=2
            j+=2
        
        
        #print("end up ",nums, i, j)
        
        return nums[i]
        