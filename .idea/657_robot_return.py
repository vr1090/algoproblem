class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left =0
        top = 0
        
        dictMoves = {
            "U":(0,-1),
            "D":(0,1),
            "L":(-1,0),
            "R":(1,0)
        }
        
        for m in moves:
            addition = dictMoves[m]
            left = left + addition[0]
            top = top + addition[1]
        
        
        return left == 0 and top ==0
        