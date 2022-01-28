class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        
        # add sum for 2 array a and b
        countSumAB = {}
        for a in nums1:
            for b in nums2:
                total = a + b
                countSumAB[total] = countSumAB.get(total, 0) + 1
        
        # add sum for c and d
        for c in nums3:
            for d in nums4:
                totalSum = c + d
                needToFind = -1 * totalSum
                
                if needToFind in countSumAB:
                    ans = ans + countSumAB[needToFind]
        
        return ans
        