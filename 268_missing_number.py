class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allSum = sum(nums)
        shouldSum = len(nums) * (len(nums)+1 ) // 2
        return shouldSum - allSum