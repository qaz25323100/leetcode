class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        L = 0
        R = 0
        for i in s:
            
            if i == 'L':
                L+=1
            elif i== 'R':
                R+=1
            
            if L == R:
                counter+=1
                L = 0
                R = 0
        
        return counter

s = Solution()
print(s.balancedStringSplit("RLLLLRRRLR"))
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("LLLLRRRR"))