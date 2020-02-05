import math
class Solution:
    def minTimeToVisitAllPoints(self, points: [[int]]) -> int:
        sec = 0
        for node in range(len(points)-1):
            
            sec += max(abs(points[node+1][0]-points[node][0]),abs(points[node+1][1]-points[node][1]))
            
        return sec
s = Solution()
s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])