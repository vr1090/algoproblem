class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(nums, i ):
            if( sum(nums) == target):
                result.append(nums.copy() )
                return
            
            if sum(nums) > target :
                return
            
            if i >= len(candidates):
                return
            
            nums.append( candidates[i])
            dfs(nums, i)
            nums.pop()
            dfs(nums, i+1)
        
        dfs([],0)
        return result