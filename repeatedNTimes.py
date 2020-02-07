class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        for a in set(A):
    	    if A.count(a) != 1: 
                return a

s = Solution()

print(s.repeatedNTimes([1,2,3,3]))