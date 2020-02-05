class Solution:
    def decompressRLElist(self, nums):
        
        res = []
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                res.append(nums[i+1])

        return res
            
s = Solution()
print(s.decompressRLElist([1,2,3,4]))