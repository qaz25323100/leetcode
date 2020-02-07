class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        
        res= []
        size = len(A)
        i = 0
        while i < size:
            if A[i]%2 == 0:
                
                res.append(A[i])
                A.pop(i)
                size-=1
                i -=1
            i+=1

        res.extend(A)

        return res
s = Solution()
s.sortArrayByParity([3,1,2,4])