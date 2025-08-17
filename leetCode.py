from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] = minimum HP needed at cell (i,j) to survive
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        
        # base case: at princess position, knight needs at least 1 HP
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        
        # fill dp from bottom-right to top-left
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need
        
        return dp[0][0]
