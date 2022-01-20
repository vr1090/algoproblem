class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            second = target -nums[i]
            
            if second in hash and hash[second] != i:
                return [i, hash[second]]
        
        return [0,0]
        