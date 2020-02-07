class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        
        return sorted([i*i for i in A])
        
        
s = Solution()
s.sortedSquares([-4,-1,0,3,10])
