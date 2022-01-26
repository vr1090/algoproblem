class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}
        
        for x in nums :
            if dicts.get(x) is None:
                dicts[x] = 1
            else:
                dicts[x] = dicts[x] + 1
        
        maxKey= nums[0]
        maxCount = 0
        
        for x in dicts.items() :
            if x[1] > maxCount:
                maxKey = x[0]
                maxCount = x[1]
        
        return maxKey
        