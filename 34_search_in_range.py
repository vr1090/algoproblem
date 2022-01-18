class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if( len(nums) == 0):
            return [-1,-1]
        
        if target not in nums:
            return [-1,-1]
        
        
        begin = 0
        end = len(nums) -1
        
        while nums[begin] != target:
            # print("haha", begin, end)
            middle = ceil((begin + end)/2)
            
            if(nums[middle] == target):
                begin = middle
                break
                
            if nums[middle] < target:
                begin = middle
            else:
                end = middle
                
        
        left = begin
        right = begin
        
        while left >= 0 and left -1 >=0 and nums[left] == nums[left-1]:
            left -=1
            
        while right < len(nums) and right+1 < len(nums) and nums[right] == nums[right+1]:
            right +=1
        
        return [left,right]
        