class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newArray = []
        count =0
        
        for i in range(len(nums)):
            if nums[i] != 0 :
                newArray.append(nums[i])
                count += 1
        
        while count < len(nums):
            newArray.append(0)
            count += 1
        
        for i in range(len(newArray)):
            nums[i] = newArray[i]