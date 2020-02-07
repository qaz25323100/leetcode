class Solution:
    def sumZero(self, n: int) -> [int]:
        res = []
        for i in range(1,(n//2)+1):res.append(i)
        for i in range(-1,(-1*(n//2))-1,-1):res.append(i)
        if n%2 == 1: res.append(0)
        print(res)
        
        return res
s = Solution()
s.sumZero(5)
s.sumZero(4)