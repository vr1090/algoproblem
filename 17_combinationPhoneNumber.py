class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            if digits == "1":
                return []
            elif digits == "2":
                return ["a","b","c"]
            elif digits == "3":
                return ["d","e","f"]
            elif digits == "4":
                return ["g", "h","i"]
            elif digits == "5":
                return ["j","k","l"]
            elif digits == "6":
                return ["m","n","o"]
            elif digits == "7":
                return ["p","q","r","s"]
            elif digits =="8":
                return ["t","u","v"]
            elif digits =="9":
                return ["w","x","y","z"]
            else:
                return []
        else:
            firstDigits = self.letterCombinations( digits[0])
            secondDigits = self.letterCombinations(digits[1:])
            return [first+second for first in firstDigits for second in secondDigits    ]
        