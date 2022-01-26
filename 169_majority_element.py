class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}
        
        for x in nums :
                dicts[x] = dicts.get(x,0) + 1
        
        for x in nums:
            if dicts[x] > len(nums)//2 :
                return x
