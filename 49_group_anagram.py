class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts={}
        
        for s in strs:
            hashValue = self.calculateHash(s)
            
            if dicts.get(hashValue) is None:
                dicts[hashValue] = [s]
            else:
                dicts[hashValue].append(s)
            
    
        return dicts.values()
    
    
    def calculateHash(self, s:str)-> str:
        return "".join(sorted(s))
        