class Solution:
    def judgeCircle(self, moves: str) -> bool:

        x,y = 0,0

        for i in list(moves):
            if i == 'U':
                y+=1
            elif i == 'D':
                y-=1
            elif i == 'R':
                x+=1
            else:
                x-=1
        
        if x == 0 and y == 0:
            return True
        
        return False

s = Solution()
print(s.judgeCircle("UD"))

print(s.judgeCircle("LL"))
