class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        maxRow = len(board)        
        maxCol = len( board[0])
        
        
        if maxRow <=0 or maxCol <=0:
            return False
        
        
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            elif r < 0 or c < 0 or r >= maxRow or c >= maxCol or \
                board[r][c] != word[i] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            visited.remove((r,c))
            
            return res
        
        for i in range(maxRow):
            for j in range(maxCol):
                if dfs(i,j,0):
                    return True
        
        return False