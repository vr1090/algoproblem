class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        def setan():
            pass
        
        def getInts(s:str, i:int)->int:
            if i < 0 or i > len(s)-1:
                return 0
            elif s[i] == '1':
                return 1
            else:
                return 0

        setan()
        pA = len(a)-1
        pB = len(b) - 1
        
        result=""
        carry = 0
        
        while pA >=0 or pB >=0:
            valueA = getInts(a, pA)
            valueB = getInts(b,pB)
            totalValue = valueA + valueB + carry
            carry = (totalValue)//2
            valueAppend = (totalValue) % 2
            result = str(valueAppend) + result
            pA -=1
            pB -=1
        
        if carry == 1:
            result = "1"+ result
            carry =0
        
        return result
            
        
  